from .models import Profile, Journal
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'breathe_theme', 'breathe_count']

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'profile', 'date', 'title', 'entry', 'mood']