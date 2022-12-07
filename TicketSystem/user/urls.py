from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.userLogin, name="user-login"), 
    path('register/', views.userRegister, name="user-register"),
    path('logout/', views.userLogout, name="user-logout"), 
    
    path('profile/<str:pk>/', views.userProfile, name="user-profile")
]