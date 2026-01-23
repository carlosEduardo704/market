from .forms import CustomUserCreationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class AccountDatailView(LoginRequiredMixin, TemplateView):
    template_name = 'account_information.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'account_update_information.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('my_account')

    def get_object(self, queryset=None):
        return self.request.user