from django.db import models

class Event(models.Model):
    # --- Arabic (Main) ---
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # --- English (Optional) ---
    title_en = models.CharField(max_length=200, null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    # --- Turkish (Optional) ---
    title_tr = models.CharField(max_length=200, null=True, blank=True)
    description_tr = models.TextField(null=True, blank=True)

    # --- Common Data ---
    year = models.IntegerField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return f"{self.year} - {self.title}"