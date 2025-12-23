from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from address.models import Address
from address.forms import AddressModelForm
from django.urls import reverse_lazy


class AddressListView(CreateView):
    model = Address
    template_name = 'address.html'
    form_class = AddressModelForm
    success_url = reverse_lazy('adress_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        addresses = [address for address in Address.objects.filter(user=self.request.user)]
        context['addresses'] = addresses
        
        return context


class RemoveAddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'address.html'
    success_url = reverse_lazy('adress_list')
    
    # Restringe o queryset para que o usuário não possa deletar o endereço de outro usuário.
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)