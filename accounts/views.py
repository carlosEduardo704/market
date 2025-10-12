from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

