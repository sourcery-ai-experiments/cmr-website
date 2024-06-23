import uuid

from django.db import models


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=254)
    middleName = models.CharField(max_length=254, blank=True)
    lastName = models.CharField(max_length=254)
    email = models.EmailField(blank=True)
    birthDate = models.DateField(blank=True)
    memberDate = models.DateField(blank=True)
    renewalDate = models.DateField(blank=True)
    expireDate = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='member_profiles/', blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Member: {self.firstName} {self.lastName} [ID: {self.id}]'
