from .models import Profile, Journal
# from django.contrib.auth.models import User, Group
from rest_framework import serializers

# ========== Model Serialisers ==========
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
    
# ========== JWT ==========
class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)