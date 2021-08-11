from .models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = User.objects.all()
    # The serializer class for serializing output
    serializer_class = UserSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]