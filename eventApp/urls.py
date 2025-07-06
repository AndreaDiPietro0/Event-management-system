from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("events/", views.events, name="events"),
    path("booking/", views.booking, name="booking"),
    path("contact/", views.contact, name="contact"),
    path("create_event/", views.create_event, name="create_event"),
    path("update_event/<int:event_id>/", views.update_event, name="update_event"),
    path("delete_event/<int:event_id>/", views.delete_event, name="delete_event"),
    path("my_registrations/", views.my_registrations, name="my_registrations"),
    path("unregister_event/<int:registration_id>/", views.unregister_event, name="unregister_event"),
    path("event_attendees/<int:event_id>/", views.event_attendees, name="event_attendees"),
    path('login/', auth_views.LoginView.as_view(template_name='log.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration is handled by userapp
    # path('register/', views.reg, name='register'),

]

# Add this if not already in the project
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
