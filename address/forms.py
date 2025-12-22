from django import forms
from django.core.exceptions import ValidationError
from address.models import Address

MAX_ADDRESSES_PER_USER = 3

class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

        labels = {
            'adress_name': 'Nome',
            'street': 'Rua',
            'number': 'Número',
            'zip_code': 'CEP',
            'city': 'Cidade',
            'district': 'Municipio',
            'uf': 'Estado'
        }

        widgets = {
            "user": forms.HiddenInput(),
            "created_at": forms.HiddenInput(),
            "updated_at": forms.HiddenInput()
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()


        if not self.instance.pk and self.user:
            if Address.objects.filter(user=self.user).count() >= MAX_ADDRESSES_PER_USER:
                raise ValidationError(f"Um usuário não pode ter mais de {MAX_ADDRESSES_PER_USER} endereços cadastrados!")
        
        return cleaned_data

    def clean_user(self):
        user = self.cleaned_data.get("user")
        if not self.instance.pk:
            if Address.objects.filter(user=user).count() >= MAX_ADDRESSES_PER_USER:
                raise forms.ValidationError(f"Usuário não pode ter mais de {MAX_ADDRESSES_PER_USER} endereços cadastrados!")
        return user
    
    error_messages = {

    }