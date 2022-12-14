from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User 
import uuid 
 





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=400, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True,
                                     upload_to='profile-imgs', default='profile-imgs/avatar.svg')
    background_image = models.ImageField(null=True, blank=True,
                                     upload_to='backgrounds', default='background-imgs/default.jpg')
    social_website = models.CharField(max_length=300, null=True, blank=True)
    social_youtube = models.CharField(max_length=300, null=True, blank=True)
    social_facebook = models.CharField(max_length=300, null=True, blank=True)
    social_instagram = models.CharField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    

    

