from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
# from lepak.permissions import IsAdminOrIsSelf
from rest_framework.decorators import action
# logged_in_user = settings.AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default={"username": "test", "password": "123"})
    breathe_theme = models.CharField(default="Box", max_length=50)
    breathe_count = models.PositiveSmallIntegerField(default=1)
    # journals = serializers.PrimaryKeyRelatedField(many=True, queryset=Journal.objects.all())

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # @action(detail=True, methods=['get'])
    # def journals(self, request, pk=None):
    #     return self
        # Journal.objects.create()

class Journal(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="journals")
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    entry = models.TextField(blank=True)
    mood = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    def save(self, request, *args, **kwargs):
        print(request.user)
        self.profile = request.user
        super(Journal, self).save(*args, **kwargs)