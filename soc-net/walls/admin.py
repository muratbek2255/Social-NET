from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from walls.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("customuser", "published", "created_at", "moderat", "views_count", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    mptt_level_indent = 15
