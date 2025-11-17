from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Django-Views
from django.views.generic.edit import FormView
# Models
from cart.models import Cart
from order.models import Order, OrderItem
# Forms
from order.forms import OrderModelForm
# Create your views here.


class CheckoutFormView(LoginRequiredMixin, FormView):
    template_name = 'checkout.html'
    form_class = OrderModelForm
    success_url = '/'

    def get_cart(self):
        if self.request.user.is_authenticated:
            try:
                return Cart.objects.get(usuario=self.request.user)
            except Cart.DoesNotExist:
                return None

        return None

    
    def form_valid(self, form):
        cart = self.get_cart()

        if not cart or not cart.itens.exists():
            return redirect('/')

        with transaction.atomic():

            new_order = form.save(commit=False)
            new_order.save()

            total_order = 0

            for cart_item in cart.itens.all():
                
                unitary_price = cart_item.product.price


                OrderItem.objects.create(
                    order = new_order,
                    product = cart_item.product,
                    quantity = cart_item.quantity,
                    product_price = cart_item.get_subtotal
                )

                total_order += cart_item.quantity * unitary_price

            
            new_order.total = total_order
            new_order.save()

            cart.itens.all().delete()

            return redirect('/')

        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Adiciona o objeto carrinho para que o template possa listar os itens
        context['cart'] = self.get_cart()
        
        return context
