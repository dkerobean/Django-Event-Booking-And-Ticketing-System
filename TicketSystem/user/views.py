from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile



def userLogin(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or Password is incorrect")
    
    context = {
        'page':page
    }
    
    return render(request, 'user/login_register.html',context)


def userRegister(request):
    
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            
            login(request, user)
            return redirect('/')
            
    context  = {
        'form':form
    }

    return render(request, 'user/login_register.html', context)


def userLogout(request):
    logout(request)
    return redirect('/')


def userProfile(request, pk):
    
    profiles = request.user.profile
    profile = User.objects.get(id=pk)
    
    
    context = {
        'profile':profiles
    }
    
    return render(request, 'user/user-profile.html', context)



