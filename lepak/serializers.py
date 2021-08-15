from .models import Profile, Journal
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
    
    # def create(self, request):
        # journal = Journal.objects.create(
        #     title = validated_data['title'],
        #     entry = validated_data['entry'],
        #     mood = validated_data['mood']
        # )
        # serializer = self.get_serializer(data=request.data)
        # serializer.save(profile=request.user)
        # return Journal.objects.create()