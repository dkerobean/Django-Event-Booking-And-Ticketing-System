from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.userLogin, name="user-login"), 
    path('register/', views.userRegister, name="user-register"),
    path('logout/', views.userLogout, name="user-logout"), 
    
    path('profile/<str:pk>/', views.userProfile, name="user-profile"), 
    path('profile/organizer/<str:pk>/', views.organizerProfile, name="organizer-profile"),
    
    path('dashboard/', views.organizerDashboard, name="organizer-dashboard"), 
    path('dashboard/events/', views.eventDashboard, name="event-dashboard"),
]