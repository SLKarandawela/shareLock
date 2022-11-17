from django.urls import path
from system_user.views import AuthUserLoginView, AuthUserRegistrationView, UserListView

urlpatterns = [
    path('register', AuthUserRegistrationView.as_view(), name='register'),
    path('login', AuthUserLoginView.as_view(), name='login'),
    path('users', UserListView.as_view(), name='users')
]