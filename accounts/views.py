from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def register_view(request):
    if request.method =='POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('home_page')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

