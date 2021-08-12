from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default={"username": "test", "password": "123"})
    breathe_theme = models.CharField(default="Box", max_length=50)
    breathe_count = models.PositiveSmallIntegerField(default=1)
    # journals = models.OneToOneField(Journal, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Journal(models.Model):
    # profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    entry = models.TextField(blank=True)
    mood = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])