from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView, DetailView

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