from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def home_page(request):
    return render('/dashboard')

@login_required(login_url='/login')
def users_page(request):
    users = User.objects.all()
    return render(request, 'main/home.html', {'users': users})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})