from django.contrib import admin

from followers.models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'subscriber']
