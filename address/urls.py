from django.urls import path
from address.views import AddressListView, RemoveAddressDeleteView, CreateAdressView, UpdateAddressView


urlpatterns = [
    path('addresses/', AddressListView.as_view(), name='adress_list'),
    path('addresses/<int:pk>/delete/', RemoveAddressDeleteView.as_view(), name='delete_address'),
    path('addresses/create_address', CreateAdressView.as_view(), name='create_address'),
    path('addresses/update_address/<int:pk>', UpdateAddressView.as_view(), name='update_address')
]