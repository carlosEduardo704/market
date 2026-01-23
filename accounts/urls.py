from django.urls import path

from accounts.views import RegisterView, AccountDatailView, UserUpdateView
from django.contrib.auth import views as auth_views
from accounts.forms import CustomAuthenticationForm

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', form_class=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('my_account/', AccountDatailView.as_view(), name='my_account'),
    path('my_account/update_information/<int:pk>', UserUpdateView.as_view(), name='user_update_information')
]