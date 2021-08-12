from .models import Journal
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'date', 'title', 'entry', 'mood']