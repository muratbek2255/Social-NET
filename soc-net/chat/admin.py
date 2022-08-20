from django.contrib import admin
from django.contrib.auth import get_user_model

from chat.models import Message, Room

User = get_user_model()


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
