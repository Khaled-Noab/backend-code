import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from api.models import Event

class Command(BaseCommand):
    help = 'Imports events from timeline_data.json into the database'

    def handle(self, *args, **kwargs):
        # 1. Find the file
        file_path = os.path.join(settings.BASE_DIR, 'api', 'timeline_data.json')
        
        # 2. Open the file (handling Arabic text)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                events_list = data['events'] # Access the list inside the JSON
                
                self.stdout.write(f"Found {len(events_list)} events. Importing now...")

                # 3. Save each event to the Database
                for item in events_list:
                    # Check if it already exists to avoid duplicates
                    if not Event.objects.filter(year=item['year'], title=item['title']).exists():
                        Event.objects.create(
                            year=item['year'],
                            title=item['title'],
                            description=item['description']
                        )
                        print(f"Saved: {item['title']}")
                    else:
                        print(f"Skipped (Already exists): {item['title']}")

            self.stdout.write(self.style.SUCCESS('Success! All events imported.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Error: Could not find timeline_data.json'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))