from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            login(request, user)
            return redirect('home_page')
        else:
            CustomAuthenticationForm()
    else:
        login_form = CustomAuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def register_view(request):
    if request.method =='POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('home_page')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def logout_view(request):
    logout(request)
    return redirect('home_page')