from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - ${self.price} for {self.duration_days} days"