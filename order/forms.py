from django import forms
from order.models import Order
from address.models import Address

class OrderModelForm(forms.ModelForm):
    address = forms.ModelChoiceField(
        widget=forms.RadioSelect,
        queryset=Address.objects.none(),
        empty_label=None,
        label='Escolha um endereço'
    )

    class Meta:
        model = Order
        fields = ['payment_method']

        widgets = {
            'payment_method': forms.Select
        }

    # filtra o queryset para que só mostre os endereços do usuário
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address"].queryset = Address.objects.filter(user=user)
