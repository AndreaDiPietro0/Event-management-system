from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    image = models.URLField(max_length=500, default='https://placehold.co/600x400', blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events', null=True)

    def __str__(self):
        return self.name

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_registrations')
    user_phone = models.CharField(max_length=10)
    registration_date = models.DateField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
