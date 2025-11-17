from django import forms
from order.models import Order


class OrderModelForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['payment_method']

        widgets = {
            'payment_method': forms.Select
        }
