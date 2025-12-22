# File: api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL for all events: /api/events/
    path('events/', views.get_all_events, name='all-events'),
    
    # URL for one event: /api/events/1/
    path('events/<int:event_id>/', views.get_event_by_id, name='event-detail'),
]