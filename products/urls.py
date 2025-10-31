from django.urls import path

from products.views import ProductListView, ProducDetailView, ProductCreateView, ProductUpdateView
from django.views.generic import TemplateView, DetailView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/<str:bar_code>/', ProducDetailView.as_view(), name='product_detail'),
    path('new_product/', ProductCreateView.as_view(), name='new_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='product_update')
]