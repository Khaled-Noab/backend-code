from django.db import models

class Event(models.Model):
    year = models.CharField(max_length=10)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    # Arabic (We keep the old names for Arabic to save your current data)
    title = models.CharField(max_length=200) 
    description = models.TextField()

    # English (New!)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    # Turkish (New!)
    title_tr = models.CharField(max_length=200, blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title