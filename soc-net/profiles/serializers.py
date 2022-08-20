from rest_framework import serializers

from profiles.models import CustomUser


class CustomUserPublicSerializer(serializers.ModelSerializer):
    """Вывод информации о кастомном пользователе"""
    class Meta:
        model = CustomUser
        exclude = ("email", "number_phone", "password", "last_login", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")


class CustomUserSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        exclude = ("password", "number_phone", "last_login", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")


class UserByFollowers(serializers.ModelSerializer):

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'avatar')
