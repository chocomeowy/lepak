from django.contrib.auth import authenticate, login
from django.http import JsonResponse
# from django.contrib.auth.models import User
from .models import Profile, Journal
from rest_framework import viewsets, permissions, response, status, generics
# from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .serializers import TokenSerializer, JournalSerializer, ProfileSerializer, MyTokenObtainPairSerializer

# ========== Model Viewsets ==========
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, format='json'):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            return Response(
                data={
                    "message": "Request is invalid."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, format='json'):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            journal = serializer.save()
            if journal:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            return Response(
                data={
                    "message": "Journal entry not valid. Please indicate your mood."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        obj = Journal.objects.filter(profile=self.request.user)
        return obj


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
                "token": str(refresh.access_token),
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
                    "message": "Username and password is required to register a user."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        elif Profile.objects.get(username=username):
            return Response(
                data={
                    "message": "Username already exists."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        new_user = Profile.objects.create_user(
            username=username, password=password
        )
        return Response(status=status.HTTP_201_CREATED)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # try:
        #     serializer.is_valid(raise_exception=True)
        # except TokenError as e:
        #     return Response(
        #         data={
        #             "message": "Invalid token."
        #         },
        #         status=status.HTTP_401_UNAUTHORIZED
        #     )

        if not serializer.is_valid():
            return Response(
                data={
                    "message": "Unable to log in. Please try again."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

