import uuid

from django.db import models


class RoadName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    shortName = models.CharField(max_length=10, blank=True)
    code = models.CharField(max_length=4, blank=True)
    logo = models.ImageField(upload_to='roadname_logos/', blank=True)
    wikipedia = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Road Name: {self.name} ({self.shortName}) [ID: {self.id}]'
