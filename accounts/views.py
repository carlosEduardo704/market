from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Order, OrderItem

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class AccountDatailView(LoginRequiredMixin, TemplateView):
    template_name = 'my_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        orders = []
        for order in Order.objects.filter(user=self.request.user):
            orders.append(order)

        context['orders'] = orders

        return context