from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 
            'year', 
            'image',
            # Arabic (Main)
            'title', 
            'description',
            # English (New)
            'title_en', 
            'description_en',
            # Turkish (New)
            'title_tr', 
            'description_tr'
        ]