import labels
from django import forms
from .models import Registration, Event

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['user_phone', 'event']

        labels={
            'user_phone':'Phone:',
            'event':'Event:',
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']

        labels={
            'name':'Event Name:',
            'description':'Description:',
            'date':'Date:',
            'time':'Time:',
            'venue':'Venue:',
            'image':'Image:',
        }
