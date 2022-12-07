from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name="home"),
    
    path('create-event', views.createEvent, name="create-event"),
    path('online-event', views.createOnlineEvent, name="online-event"),
    path('venue-event', views.createVenueEvent, name="venue-event"),
    
    path('events', views.allEvents, name="events"),



]