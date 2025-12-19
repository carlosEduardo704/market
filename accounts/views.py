from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Order, OrderItem
from accounts.mixins import RestrictUserMixin

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class AccountDatailView(LoginRequiredMixin, TemplateView):
    template_name = 'account_information.html'


class OrdersView(LoginRequiredMixin, TemplateView):
    model = Order
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        orders = [order for order in Order.objects.filter(user=self.request.user)]
        context['orders'] = orders

        return context


class OrderDetailView(RestrictUserMixin, LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_itens = [item for item in OrderItem.objects.filter(order=self.kwargs['pk'])]
        context['items'] = order_itens
        
        return context

class AdressDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'adresses.html'