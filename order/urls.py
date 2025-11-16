from django.urls import path
from order.views import CheckoutListView


urlpatterns = [
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
]