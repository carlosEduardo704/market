from django import forms
from address.models import Address, MAX_ADDRESSES_PER_USER


class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"

        widgets = {
            "user": forms.HiddenInput(),
            "created_at": forms.HiddenInput(),
            "updated_at": forms.HiddenInput()
        }

    def clean_user(self):
        user = self.cleaned_data.get("user")
        if not self.instance.pk:
            if Address.objects.filter(user=user).count() >= MAX_ADDRESSES_PER_USER:
                raise forms.ValidationError(f"Usuário não pode ter mais de {MAX_ADDRESSES_PER_USER} endereços cadastrados!")
        return user