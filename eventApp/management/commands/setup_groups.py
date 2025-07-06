from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from eventApp.models import Event, Registration

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **options):
        # Create groups
        attendee_group, created = Group.objects.get_or_create(name='Attendee')
        organizer_group, created = Group.objects.get_or_create(name='Organizer')
        
        # Get content types
        event_content_type = ContentType.objects.get_for_model(Event)
        registration_content_type = ContentType.objects.get_for_model(Registration)
        
        # Define permissions for Attendee group
        view_event_perm = Permission.objects.get(content_type=event_content_type, codename='view_event')
        add_registration_perm = Permission.objects.get(content_type=registration_content_type, codename='add_registration')
        view_registration_perm = Permission.objects.get(content_type=registration_content_type, codename='view_registration')
        delete_registration_perm = Permission.objects.get(content_type=registration_content_type, codename='delete_registration')
        
        # Assign permissions to Attendee group
        attendee_group.permissions.add(view_event_perm)
        attendee_group.permissions.add(add_registration_perm)
        attendee_group.permissions.add(view_registration_perm)
        attendee_group.permissions.add(delete_registration_perm)
        
        # Define additional permissions for Organizer group
        add_event_perm = Permission.objects.get(content_type=event_content_type, codename='add_event')
        change_event_perm = Permission.objects.get(content_type=event_content_type, codename='change_event')
        delete_event_perm = Permission.objects.get(content_type=event_content_type, codename='delete_event')
        
        # Assign permissions to Organizer group (includes Attendee permissions)
        organizer_group.permissions.add(view_event_perm)
        organizer_group.permissions.add(add_registration_perm)
        organizer_group.permissions.add(view_registration_perm)
        organizer_group.permissions.add(delete_registration_perm)
        organizer_group.permissions.add(add_event_perm)
        organizer_group.permissions.add(change_event_perm)
        organizer_group.permissions.add(delete_event_perm)
        
        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))