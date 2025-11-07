from django.shortcuts import render
from products.models import Product
from .forms import ProductModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .filters import ProductFilter

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(department=True)

    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filtro = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['products'] = filtro.qs
        context['filtro'] = filtro

        return context

class ProducDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('products.add_Product', 'products.add_Brand')
    model = Product
    template_name = "new_product.html"
    form_class = ProductModelForm
    success_url = '/products/'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('products.change_Product', 'products.change_Brand')
    model = Product
    template_name = 'edit_product.html'
    context_object_name = 'products'
    form_class = ProductModelForm
    
    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk, 'bar_code': self.object.bar_code} )