from django.shortcuts import render
from products.models import Product
from .forms import ProductModelForm
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')

        if search:
            products =products.filter(name__icontains=search)

        return products


class ProducDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('products.add_Product', 'products.add_Brand')
    model = Product
    template_name = "new_product.html"
    form_class = ProductModelForm
    success_url = '/products/'