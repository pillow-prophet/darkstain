from django.urls import path

from api.views.auth import LoginView, RefreshView
from api.views.users import RegisterView, UserListView

urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/refresh/', RefreshView.as_view(), name='refresh'),
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/', UserListView.as_view(), name='user-list'),
]