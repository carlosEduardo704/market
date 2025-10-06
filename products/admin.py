from django.contrib import admin
from products.models import Department, Product

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'price', 'bar_code')
    search_fields = ('name', 'department', 'bar_code')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
