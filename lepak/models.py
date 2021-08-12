from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    breathe_theme = models.CharField(default="Box", max_length=50)
    breathe_count = models.PositiveSmallIntegerField(default=0)
    # journals = models.OneToOneField(Journal, on_delete=models.CASCADE)

class Journal(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    entry = models.TextField(blank=True)
    mood = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])