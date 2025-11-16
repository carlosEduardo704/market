from django.urls import path
from order.views import CheckoutFormView


urlpatterns = [
    path('checkout/', CheckoutFormView.as_view(), name='checkout'),
]