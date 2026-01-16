from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from order.mixins import RestrictUserMixin
from django.urls import reverse_lazy
# Django-Views
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
# Models
from cart.models import Cart
from order.models import Order, OrderItem
from address.models import Address
# Forms
from order.forms import OrderModelForm
from address.forms import AddressModelForm
# Create your views here.


class CheckoutFormView(LoginRequiredMixin, FormView):
    template_name = 'checkout.html'
    form_class = OrderModelForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
        
    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.objects.pk})

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
            address = form.cleaned_data["address"]

            form.instance.user = self.request.user
            form.instance.shipping_street = address.street
            form.instance.shipping_number = address.number
            form.instance.shipping_zip_code = address.zip_code
            form.instance.shipping_city = address.city
            form.instance.shipping_quartier = address.district
            form.instance.shipping_uf = address.uf

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

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Adiciona o objeto carrinho para que o template possa listar os itens.
        context['cart'] = self.get_cart()
        # context com endereços do usuário.
        context['addresses'] = Address.objects.filter(user=self.request.user)
        # context de endereços do usuário para serem usados no form de conclusão de venda.
        context['form_addresses'] = self.form_class(
            user=self.request.user
        ).fields["address"].queryset
        
        return context


class OrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)



class OrderDetailView(RestrictUserMixin, LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_itens = [item for item in OrderItem.objects.filter(order=self.kwargs['pk'])]
        context['items'] = order_itens
        
        return context