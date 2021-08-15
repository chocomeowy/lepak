from django.urls import path
from .views import ProfileViewSet, JournalViewSet, LoginView, RegisterUsersView

app_name = 'lepak'

urlpatterns = [
    path('user/', ProfileViewSet.as_view(), name='users'),
    path('journal/', JournalViewSet.as_view(), name='journals'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('signup/', RegisterUsersView.as_view(), name='user_signup')
]