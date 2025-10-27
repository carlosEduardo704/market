from django.db import models
from django.conf import settings 
from products.models import Product


class Cart(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrinho')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        return sum(item.get_subtotal for item in self.itens.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='itens')
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Altere 'app_produtos.Produto'
    quantity = models.IntegerField(default=1)
    
    @property
    def get_subtotal(self):
        # Assumindo que seu Produto tem um campo 'preco'
        return self.product.price * self.quantity