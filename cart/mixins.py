from django.shortcuts import get_object_or_404
from .models import Cart

class CartMixin:
    """Mixin para garantir que o usuário logado tenha um objeto Carrinho."""
    
    def get_cart(self):
        """Retorna o carrinho do usuário, criando um se não existir."""
        
        if self.request.user.is_authenticated:
            # Tenta obter ou cria um novo carrinho para o usuário
            cart, created = Cart.objects.get_or_create(usuario=self.request.user)
            return cart
        
        # Para usuários anônimos (sem logar), a lógica de sessão seria aplicada aqui.
        return None