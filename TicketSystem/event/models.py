from django.db import models
from user.models import Profile 
import uuid 


class Event(models.Model):
    organizer = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=700, null=True)
    category = models.CharField(max_length=100, null=True)
    event_type = models.CharField(max_length=100, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    gps_location = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    total_tickets = models.IntegerField(null=True, blank=True)
    participants = models.ManyToManyField(Profile,
                                        blank=True, related_name="participants")
    event_location = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="event-imgs", default='event-imgs/img-8.jpg')
    event_date = models.DateTimeField(null=True, blank=True)
    event_time = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__ (self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created_at']
    
    
