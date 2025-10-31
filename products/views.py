from django.shortcuts import render
from products.models import Product
from .forms import ProductModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy

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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'edit_product.html'
    context_object_name = 'products'
    form_class = ProductModelForm
    
    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk, 'bar_code': self.object.bar_code} )