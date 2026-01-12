from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from address.models import Address
from address.forms import AddressModelForm
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme


class AddressListView(ListView):
    model = Address
    template_name = 'address.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        addresses = [address for address in Address.objects.filter(user=self.request.user)]
        context['addresses'] = addresses
        
        return context


class CreateAdressView(CreateView):
    model = Address
    template_name = 'create_address.html'
    form_class = AddressModelForm
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')

        if next_url and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={self.request.get_host()}):
            return next_url

        return super().get_success_url()


class UpdateAddressView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Address
    template_name = 'update_address.html'
    context_object_name = 'addresses'
    permission_required = ('addresses.change_Address')
    form_class = AddressModelForm
    success_url = reverse_lazy('adress_list')
    
    # Restringe o queryset para que o usuário não possa deletar o endereço de outro usuário.
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class RemoveAddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'address.html'
    success_url = reverse_lazy('adress_list')
    
    # Restringe o queryset para que o usuário não possa deletar o endereço de outro usuário.
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
