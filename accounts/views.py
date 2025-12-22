from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class AccountDatailView(LoginRequiredMixin, TemplateView):
    template_name = 'account_information.html'
