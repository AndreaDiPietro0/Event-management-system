# Event Management System

A Django-based event management system that allows users to create, view, and register for events.

## Features

- User authentication (login, logout, registration)
- Two user roles with distinct permissions:
  - **Attendee**: Can view events, register/unregister for events, and view their own registrations
  - **Organizer**: Has all attendee permissions, plus can create, update, and delete their own events, and view the list of attendees for their events
- Event creation and management
- Event registration and attendance tracking

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```
   python manage.py migrate
   ```
4. Set up user groups and permissions:
   ```
   python manage.py setup_groups
   ```
5. (Optional) Create test users:
   ```
   python manage.py setup_test_users
   ```
   This creates two users:
   - Attendee: username `attendee`, password `attendee123`
   - Organizer: username `organizer`, password `organizer123`
6. Run the development server:
   ```
   python manage.py runserver
   ```

## User Roles and Permissions

### Attendee
- View events
- Register for events
- Unregister from events
- View own registrations

### Organizer
- All Attendee permissions
- Create new events
- Update own events
- Delete own events
- View list of attendees for own events

## Usage

1. Register as a new user or log in with an existing account
2. Browse events on the Events page
3. Register for events you want to attend
4. View your registrations on the My Registrations page
5. If you're an Organizer, you can create new events and manage your events

## Adding Users to Groups

To add a user to a group:

1. Create a user through the registration page
2. Log in as an admin
3. Go to the admin panel
4. Navigate to Users
5. Select the user
6. Assign the user to either the Attendee or Organizer group