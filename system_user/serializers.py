from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from system_user.models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_admin',
            'is_manager'
        )

    def create(self, validated_data):
        auth_user = CustomUser.objects.create_user(**validated_data)
        return auth_user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'is_admin',
            'is_manager',
            'is_worker'
        )
