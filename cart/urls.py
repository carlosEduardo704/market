from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView, DecreaseItemQuantityView, RemoveAllItensFromCartView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart'),
    path('add/<int:produto_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('decrease/<int:item_id>/', DecreaseItemQuantityView.as_view(), name='decrease_quantity'),
    path('remove_all/<int:cart_id>', RemoveAllItensFromCartView.as_view(), name='remove_all_itens_from_cart')
]