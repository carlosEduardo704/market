from django.urls import path
from address.views import AddressListView, RemoveAddressDeleteView


urlpatterns = [
    path('addresses/', AddressListView.as_view(), name='adress_list'),
    path('addresses/<int:pk>/delete/', RemoveAddressDeleteView.as_view(), name='delete_address')
]