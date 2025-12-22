from django.urls import path
from address.views import AddressListView


urlpatterns = [
    path('addresses/', AddressListView.as_view(), name='adress_list'),
]