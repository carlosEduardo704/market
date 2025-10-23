from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static, settings
from django.views.generic import TemplateView
from products.models import Product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html', extra_context={'products': Product.objects.all()}), name='home_page'),
    path('', include('accounts.urls')),
    path('', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
