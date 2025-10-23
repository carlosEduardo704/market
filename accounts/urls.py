from django.urls import path

from accounts.views import RegisterView
from django.contrib.auth import views as auth_views
from accounts.forms import CustomAuthenticationForm

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', form_class=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]