from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from profiles.models import CustomUser
from profiles.serializers import CustomUserPublicSerializer, CustomUserSerializer


class CustomUserPublicView(ModelViewSet):
    """ Вывод публичного кастомного пользователя
    """
    queryset = CustomUser.objects.select_related('gender').all()
    serializer_class = CustomUserPublicSerializer
    permission_classes = [permissions.AllowAny]


class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
