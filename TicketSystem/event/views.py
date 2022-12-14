from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from user.models import Profile
from .forms import EventForm, VenueEvent
from django.contrib import messages

from django.db.models import Q


def home(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    events = Event.objects.all()
    
    context = {
        'profile':profile,
        'user':user, 
        'events':events
    }
    
    return render(request, 'event/home.html', context)


@login_required(login_url="user-login")
def createEvent(request):
    profile = request.user.profile
    
    context = {
        'profile':profile
    }
    
    return render(request, 'event/create-event.html', context)



@login_required(login_url="user-login")
def createOnlineEvent(request):
    
    profile = request.user.profile
    form = EventForm()
    
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = profile 
            event.location = "online"
            event.event_type = "Online"
            event.save()
            messages.success(request, 'Event Created Successfully')
            return redirect('/')
             
    context = {
        'form':form,
        'profile':profile
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
            event.event_type = "Venue"
            event.save()
            messages.success(request, 'Event Created Successfully')
            return redirect('/')
        
    context = {
        'form': form,
        'profile':profile
    }
            
    return render(request, 'event/venue-event.html', context)


def allEvents(request):
    
    profile = request.user.profile
    
    
    search_query = " "
    
    if request.GET.get('q'):
        search_query = request.GET.get('q')
           
    events = Event.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query)
    )
        
    
    context = {
        'events':events,
        'profile':profile,
        'search_query': search_query
    }
    
    
    return render(request, 'event/events.html', context)


def eventDetail(request,pk):
    
    profile = request.user.profile
    event = Event.objects.get(id=pk)
    
    
    context ={
        'profile':profile,
        'event':event
    }
    
    return render(request, 'event/event-detail.html', context)


@login_required(login_url="user-login")
def deleteEvent(request,pk):
    
    profile = request.user.profile 
    event = Event.objects.get(id=pk)
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event Deleted Successfully')
        return redirect('event-dashboard')
    
    context = {
        'object':event,
        'profile':profile
    }
    
    return render(request, 'delete.html', context)


@login_required(login_url="user-login")
def updateEvent(request,pk):
    
    profile = request.user.profile
    event = Event.objects.get(id=pk)
    
    form = EventForm(instance=event)
    
    if request.method == "POST":
        form = VenueEvent(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event Updated Successfully')
            return redirect('event-dashboard')
        
    context = {
        'profile':profile, 
        'form':form
    }

    return render(request, 'user/update-event.html', context)


@login_required(login_url="user-login")
def checkout(request, pk):
    
    profile = request.user.profile
    event = Event.objects.get(id=pk)
    
    

    if request.method == 'POST':
        event.participants.add(profile) 
        messages.success(request, 'Event Booked Successfully')
        return redirect('confirm-booking')
    
    
    context = {
        'profile': profile,
        'event': event, 
    }

    return render(request, 'event/checkout.html', context)


@login_required(login_url="user-login")
def bookingConfirm(request):
    
    profile = request.user.profile
    
    context = {
        'profile':profile
        
    }
    
    
    return render(request, 'event/booking-confirmed.html',context)
