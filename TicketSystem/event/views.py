from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from user.models import Profile
from .forms import EventForm, VenueEvent

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
            event.save()
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
            event.save()
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
def checkout(request, pk):
    
    profile = request.user.profile
    event = Event.objects.get(id=pk)
    
    

    if request.method == 'POST':
        event.participants.add(profile)
        return redirect('confirm-booking')
    
    
    context = {
        'profile': profile,
        'event': event
    }

    
    
    return render(request, 'event/checkout.html', context)


@login_required(login_url="user-login")
def bookingConfirm(request):
    
    profile = request.user.profile
    
    context = {
        'profile':profile
    }
    
    
    return render(request, 'event/booking-confirmed.html',context)
