from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from event.models import Event
from django.contrib import messages

from django.db.models import Q



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
            messages.success(request, "Login Success")
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
            messages.success(request, "User Created")
            return redirect('/')
            
    context  = {
        'form':form
    }

    return render(request, 'user/login_register.html', context)


def userLogout(request):
    logout(request)
    messages.error(request, 'Logged Out')
    return redirect('/')


def updateUser(request):
    
    profile = request.user.profile
    form = UpdateUserForm(instance=profile)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            messages.success('Updated Successfully')
            return redirect('user-profile')
            
                   
    context = {
        'form':form, 
        'profile':profile
    }
    
    return render(request, 'user/user-profile.html', context)



def userProfile(request, pk):
    
    profiles = request.user.profile
    profile = User.objects.get(id=pk)
    organised_event = Event.objects.filter(organizer__name=profiles.name) 
    attending_event = Event.objects.filter(participants__name=profiles.name)

    form = UpdateUserForm(instance=profiles)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid:
            form.save()
            messages.success(request, 'Update Successfull')
            return redirect('user-profile', profile.id)
    
    context = {
        'profile':profiles, 
        'form':form, 
        'organised_event':organised_event, 
        'attending_event': attending_event, 
        
    }
    
    return render(request, 'user/user-profile.html', context)


def organizerProfile(request, pk):
    
    profile = request.user.profile 
    
    organizer = Profile.objects.get(id=pk)
    
    organizer_events = organizer.event_set.all()
    
    context = {
        'profile':profile, 
        'organizer':organizer, 
        'organizer_events': organizer_events
    }
    
    return render(request, 'user/organizer-profile.html', context)


def organizerDashboard(request):

    profile = request.user.profile
    organizer_events = profile.event_set.all()

    context = {
        'profile': profile,
        'organizer_events': organizer_events
    }

    return render(request, 'user/organizer-dashboard.html', context)


def eventDashboard(request):
    
    q = " "

    event = Event.objects.all()
    profile = request.user.profile
    organizer_events = profile.event_set.all()
    
    
    if request.GET.get('q'):
        q = request.GET.get("q")
        organizer_events = profile.event_set.filter(
            title__icontains=q
        )
    

    context = {
        'profile': profile,
        'organizer_events': organizer_events, 
        'q':q
        
    }

    return render(request, 'user/event-dashboard.html', context)










    



