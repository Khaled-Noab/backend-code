from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

# 1. Get ALL events
@api_view(['GET'])
def get_all_events(request):
    """
    Fetch events with filters:
    - /api/events/?search=War  (Search by title)
    - /api/events/?start=1950&end=1970 (Search by year range)
    """
    # 1. Start with ALL events sorted by year
    events = Event.objects.all().order_by('year')
    
    # 2. Check for Text Search
    query = request.query_params.get('search', None)
    if query:
        events = events.filter(title__contains=query)

    # 3. Check for Year Range (New Feature!)
    start_year = request.query_params.get('start', None)
    end_year = request.query_params.get('end', None)

    if start_year and end_year:
        events = events.filter(year__gte=start_year, year__lte=end_year)

    # 4. Convert to JSON
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

# 2. Get ONE event (The missing function!)
@api_view(['GET'])
def get_event_by_id(request, event_id):
    """
    Fetch a single event by its ID.
    Usage: /api/events/1/
    """
    try:
        event = Event.objects.get(id=event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)