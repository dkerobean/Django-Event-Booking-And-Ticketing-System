from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.getRoutes),
    path('get-events/', views.getEvents),
    path('add-events/', views.addEvents),
    
    path('event/<str:pk>/', views.eventDetail),


]