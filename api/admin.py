from django.contrib import admin
from .models import Event

# Method 1: The Simple Way (Shows EVERYTHING automatically)
admin.site.register(Event)