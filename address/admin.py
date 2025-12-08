from django.contrib import admin
from address.models import Adress
from address.forms import AdressModelForm

class AdressAdmin(admin.ModelAdmin):
    form = AdressModelForm
    list_display = ("user", "address_name", "street", "city")
