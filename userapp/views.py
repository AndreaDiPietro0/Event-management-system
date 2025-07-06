from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from eventApp.views import create_groups

# Create your views here.
def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user_reg=User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()

                # Get the selected role from the form
                role = request.POST.get('role', 'Attendee')  # Default to Attendee if not specified

                # Ensure groups exist before assigning users to them
                create_groups()

                # Add user to the appropriate group based on role
                try:
                    group = Group.objects.get(name=role)
                    user_reg.groups.add(group)
                    print(f"User {user_reg.username} added to {role} group")  # Debug print
                except Group.DoesNotExist:
                    # If the group doesn't exist, log the error but continue
                    # This ensures the registration process doesn't fail if the group doesn't exist
                    print(f"{role} group does not exist. User registered without group assignment.")

                messages.success(request, f'Registration successful as {role}! Please login.')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    return render(request, 'reg.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        # Add debug messages
        messages.info(request, f'Attempting to login with username: {username}')

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'log.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'you logged out')
    return redirect('events')

@login_required(login_url='login')
def account(request):
    return render(request, 'account.html')
