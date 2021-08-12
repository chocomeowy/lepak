from .models import User, Journal
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, JournalSerializer

class UserViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = User.objects.all()
    # The serializer class for serializing output
    serializer_class = UserSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.AllowAny]