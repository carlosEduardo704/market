from django.contrib import admin
from address.models import Address
from address.forms import AddressModelForm

class AdressAdmin(admin.ModelAdmin):
    form = AddressModelForm
    list_display = ("user", "address_name", "street", "city")
