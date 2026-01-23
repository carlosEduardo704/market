from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')


class CustomAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Usuário ou senha inválidos. Por favor, tente novamente!',
        'inactive': 'Usuário inativo. Por favor, contate o suporte!'
    }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email'
        }