from django.forms import ModelForm 
from .models import Event 


class EventForm(ModelForm):
    class Meta: 
        model = Event
        fields = [
            'title','description','event_date','category','description','price',
            'total_tickets','event_time','event_location','duration','image'
        ]
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control h_50'})
            
            self.fields["event_date"].widget.attrs.update(
                {'class': 'datepicker-here'})
            
            
            
class VenueEvent(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'event_date', 'category', 'description', 'price',
            'total_tickets', 'event_time', 'duration', 'image'
        ]

    def __init__(self, *args, **kwargs):
        super(VenueEvent, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control h_50'})

             
    
