from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from address.models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address.html'