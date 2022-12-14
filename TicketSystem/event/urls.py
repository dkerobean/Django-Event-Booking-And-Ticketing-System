from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name="home"),
    
    path('create-event', views.createEvent, name="create-event"),
    path('online-event', views.createOnlineEvent, name="online-event"),
    path('venue-event', views.createVenueEvent, name="venue-event"),
    
    path('events', views.allEvents, name="events"),
    path('event/delete/<str:pk>/', views.deleteEvent, name="delete-event"),
    path('event/update/<str:pk>/', views.updateEvent, name="update-event"),
    path('event/<str:pk>/', views.eventDetail, name="event-detail"),
    
    
    path('checkout/<str:pk>/', views.checkout, name="checkout"),
    path('booking-confirmed/', views.bookingConfirm, name="confirm-booking"),





]