from django.db import models
from django.conf import settings
from cart.models import CartItem
from products.models import Product
from django.contrib.auth import settings

class Order(models.Model):
    PAYMENT_METHODS = [
        ('TICKET', 'Boleto Bancário'),
        ('CREDIT_CARD', 'Cartão de Crédito'),
        ('DEBIT_CARD', 'Cartão de Débito')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shipping_street = models.CharField(max_length=50)
    shipping_number = models.CharField(max_length=6)
    shipping_zip_code = models.CharField(max_length=9)
    shipping_city = models.CharField(max_length=29)
    shipping_quartier = models.CharField(max_length=29)
    shipping_uf = models.CharField(max_length=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='TICKET')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'product')
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} na venda #{self.order.id}"
    