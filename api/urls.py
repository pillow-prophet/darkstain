from django.urls import path

from api.views.auth import LoginView, RefreshView
from api.views.users import RegisterView, UserListView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh/', RefreshView.as_view(), name='refresh'),
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
]