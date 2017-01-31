from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Waterstand(models.Model):
    waterstand = models.FloatField(default=10)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Melding(models.Model):
    melding = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)