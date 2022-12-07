from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm, VenueEvent


def home(request):
    
    return render(request, 'event/home.html')


@login_required(login_url="user-login")
def createEvent(request):
    
    return render(request, 'event/create-event.html')



@login_required(login_url="user-login")
def createOnlineEvent(request):
    profile = request.user.profile
    form = EventForm()
    
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = profile 
            event.save()
            return redirect('/')
             
    context = {
        'form':form
    }
        
    return render(request, 'event/online-event.html', context)


@login_required(login_url="user-login")
def createVenueEvent(request):
    
    profile = request.user.profile 
    form = VenueEvent()
    
    if request.method == "POST":
        form = VenueEvent(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = profile
            event.save()
            return redirect('/')
        
    context = {
        'form': form
    }
            

    return render(request, 'event/venue-event.html', context)
