from .models import User
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']