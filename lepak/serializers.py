from .models import Profile, Journal
# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# ========== Model Serialisers ==========
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'password']

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
    
# ========== JWT ==========
class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['breathe_theme'] = user.breathe_theme
        token['breathe_count'] = user.breathe_count

        return token