from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Usuário ou senha inválidos. Por favor, tente novamente!',
        'inactive': 'Usuário inativo. Por favor, contate o suporte!'
    }
