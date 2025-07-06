from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group, User

from .forms import RegistrationForm, EventForm
from .models import Event, Registration

# Aggiungi questo all'inizio della tua view di registrazione
def create_groups():
    # Crea i gruppi se non esistono
    organizer_group, created = Group.objects.get_or_create(name='Organizer')
    attendee_group, created = Group.objects.get_or_create(name='Attendee')

# Create your views here.
def index(request):
    # Get all events for the home page
    events = Event.objects.all().order_by('-date')[:3]  # Get the 3 most recent events
    return render(request, 'index.html', {'events': events})

def about(request):
    return render(request, 'about.html')

def events(request):
    dict_event={
        'event': Event.objects.all()
    }
    return render(request, 'events.html', dict_event)

@login_required
def booking(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.save()
            messages.success(request, 'Registration successful!')
            return redirect('/')

    form = RegistrationForm()
    dict_form = {
        'form': form
    }

    return render(request, 'booking.html', dict_form)

def contact(request):
    return render(request, 'contact.html')

@login_required
def create_event(request):
    # Check if user is in Organizer group
    if not request.user.groups.filter(name='Organizer').exists():
        messages.error(request, 'You do not have permission to create events.')
        return redirect('events')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('events')
    else:
        form = EventForm()

    context = {
        'form': form
    }
    return render(request, 'create_event.html', context)

@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'my_registrations.html', {'registrations': registrations})

@login_required
def unregister_event(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id, user=request.user)
    registration.delete()
    messages.success(request, 'You have been unregistered from the event.')
    return redirect('my_registrations')

@login_required
def event_attendees(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if user is the organizer of this event
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to view attendees for this event.')
        return redirect('events')

    attendees = Registration.objects.filter(event=event)
    return render(request, 'event_attendees.html', {'event': event, 'attendees': attendees})

@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if user is in Organizer group and is the organizer of this event
    if not request.user.groups.filter(name='Organizer').exists():
        messages.error(request, 'You do not have permission to update events.')
        return redirect('events')

    if event.organizer != request.user:
        messages.error(request, 'You can only update your own events.')
        return redirect('events')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('events')
    else:
        form = EventForm(instance=event)

    context = {
        'form': form,
        'event': event
    }
    return render(request, 'update_event.html', context)

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if user is in Organizer group and is the organizer of this event
    if not request.user.groups.filter(name='Organizer').exists():
        messages.error(request, 'You do not have permission to delete events.')
        return redirect('events')

    if event.organizer != request.user:
        messages.error(request, 'You can only delete your own events.')
        return redirect('events')

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('events')

    context = {
        'event': event
    }
    return render(request, 'delete_event.html', context)


def reg(request):
    if request.method == 'POST':
        print("Form data:", request.POST)  # Debug print
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirmpassword')
        role = request.POST.get('role', 'Attendee')  # Default to Attendee if not specified

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)

                # Assign user to the selected group
                if role == 'Organizer':
                    group = Group.objects.get(name='Organizer')
                    user.groups.add(group)
                    user.save()
                    print(f"User {user.username} added to Organizer group")  # Debug print
                else:
                    group = Group.objects.get(name='Attendee')
                    user.groups.add(group)
                    user.save()
                    print(f"User {user.username} added to Attendee group")  # Debug print

                messages.success(request, f'Registration successful as {role}! Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'reg.html')