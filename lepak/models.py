from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Journal(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    entry = models.TextField(blank=True)
    mood = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])