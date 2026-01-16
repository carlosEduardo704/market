from django.urls import path
from order.views import CheckoutFormView, OrdersListView, OrderDetailView


urlpatterns = [
    path('checkout/', CheckoutFormView.as_view(), name='checkout'),
    path('orders/', OrdersListView.as_view(), name='orders'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
]