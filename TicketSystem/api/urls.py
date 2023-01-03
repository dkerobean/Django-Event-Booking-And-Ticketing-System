from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token 


urlpatterns = [
    path('', views.getRoutes),
    path('get-events/', views.getEvents),
    path('add-events/', views.addEvents),
    path('token/', obtain_auth_token, name="get-token"),
    
    path('event/<str:pk>/', views.eventDetail),


]