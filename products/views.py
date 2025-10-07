from django.shortcuts import render
from products.models import Product
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


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