from .models import Profile, Journal
from django.contrib.auth.models import update_last_login
# from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings



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
    # def validate(self, attrs):
    #     if not Profile.objects.get(username=attrs.username):
    #         return Response(
    #             data={
    #                 "message": "User does not exist."
    #             },
    #             status=status.HTTP_400_BAD_REQUEST
    #         )

    #     data = super().validate(attrs)
    #     refresh = self.get_token(self.user)

    #     data['refresh'] = str(refresh)
    #     data['access'] = str(refresh.access_token)

    #     if api_settings.UPDATE_LAST_LOGIN:
    #         update_last_login(None, self.user)

    #     return data

    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['breathe_theme'] = user.breathe_theme
        token['breathe_count'] = user.breathe_count

        return token