from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views and imports from products
from products.models import Product
from products.views import ProductListView, ProducDetailView, ProductCreateView
from django.views.generic import TemplateView, DetailView

# Views and imports from accounts
from accounts.views import RegisterView
from django.contrib.auth import views as auth_views
from accounts.forms import CustomAuthenticationForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html', extra_context={'products': Product.objects.all()}), name='home_page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', form_class=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/<str:bar_code>/', ProducDetailView.as_view(), name='product_detail'),
    path('new_product/', ProductCreateView.as_view(), name='new_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
