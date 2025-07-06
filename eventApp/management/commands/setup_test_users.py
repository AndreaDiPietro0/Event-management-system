from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create test users with different roles'

    def handle(self, *args, **options):
        # Create test users
        attendee_user, created = User.objects.get_or_create(
            username='attendee',
            defaults={
                'email': 'attendee@example.com',
                'is_active': True,
            }
        )
        
        if created:
            attendee_user.set_password('attendee123')
            attendee_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created attendee user: {attendee_user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'User {attendee_user.username} already exists'))
        
        organizer_user, created = User.objects.get_or_create(
            username='organizer',
            defaults={
                'email': 'organizer@example.com',
                'is_active': True,
            }
        )
        
        if created:
            organizer_user.set_password('organizer123')
            organizer_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created organizer user: {organizer_user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'User {organizer_user.username} already exists'))
        
        # Get groups
        try:
            attendee_group = Group.objects.get(name='Attendee')
            organizer_group = Group.objects.get(name='Organizer')
            
            # Assign users to groups
            attendee_user.groups.clear()
            attendee_user.groups.add(attendee_group)
            
            organizer_user.groups.clear()
            organizer_user.groups.add(organizer_group)
            
            self.stdout.write(self.style.SUCCESS('Successfully assigned users to groups'))
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR('Groups do not exist. Run setup_groups command first.'))