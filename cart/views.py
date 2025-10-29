from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect # Para segurança
from .models import Cart, CartItem
from products.models import Product
from .mixins import CartMixin 


class CartDetailView(LoginRequiredMixin, CartMixin, TemplateView):
    """Exibe os detalhes do carrinho de compras do usuário logado."""
    template_name = 'cart_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_cart()
        
        if cart:
            context['cart'] = cart
            context['itens'] = cart.itens.all()
        else:
            context['itens'] = [] # Carrinho vazio se não houver um objeto Cart
            
        return context


class AddToCartView(LoginRequiredMixin, CartMixin, View):
    """Adiciona um produto ao carrinho do usuário. Requer método POST."""
    
    def post(self, request, produto_id, *args, **kwargs):
        product = get_object_or_404(Product, id=produto_id)
        cart = self.get_cart()
        
        if not cart:
             # Isso só deve acontecer se o LoginRequiredMixin falhar, mas é bom prevenir
            return HttpResponseForbidden("Acesso negado: Usuário não autenticado ou carrinho inválido.") 

        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity <= 0:
                quantity = 1
        except ValueError:
            quantity = 1

        # Adicionar/Atualizar Item
        item, criado = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not criado:
            item.quantity += quantity
            item.save()
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RemoveFromCartView(LoginRequiredMixin, CartMixin, View):
    """Remove um item específico do carrinho. Requer método POST."""
    
    def post(self, request, item_id, *args, **kwargs):
        cart = self.get_cart()
        
        # Obtém o item
        item = get_object_or_404(CartItem, id=item_id)
        
        # Verifica a posse (CRÍTICO para segurança)
        if item.cart != cart:
            # Retorna 403 Forbidden se o usuário tentar remover um item que não é dele
            return HttpResponseForbidden("Acesso negado: Este item não pertence ao seu carrinho.") 
            
        # Remove Item
        item.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DecreaseItemQuantityView(LoginRequiredMixin, CartMixin, View):
    """Diminui a quantidade de um item específico do carrinho. Requer método POST."""
    
    def post(self, request, item_id, *args, **kwargs):
        cart = self.get_cart()
        
        # Obtém o item
        item = get_object_or_404(CartItem, id=item_id)
        
        # Verifica a posse (CRÍTICO para segurança)
        if item.cart != cart:
            # Retorna 403 Forbidden se o usuário tentar remover um item que não é dele
            return HttpResponseForbidden("Acesso negado: Este item não pertence ao seu carrinho.") 
        
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 