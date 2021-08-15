from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from .models import Profile, Journal
from rest_framework import viewsets, generics, permissions, status
# from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import TokenSerializer, JournalSerializer, ProfileSerializer

# ========== Model Viewsets ==========
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]


# ========== User Sessions ==========
class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # override permission class to AllowAny
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves user ID in the session using Django’s session framework
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token)
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        if not username or not password:
            return Response(
                data={
                    "message": "username and password is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = Profile.objects.create_user(
            username=username, password=password
        )
        return Response(status=status.HTTP_201_CREATED)