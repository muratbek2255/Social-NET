from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profiles.models import CustomUser, Gender


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "number_phone")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "email", "gender")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Addition info"), {"fields": ("number_phone", "avatar", )}),
    )


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        gender_count = Gender.objects.all().count()
        if gender_count >= 2:
            return False
        else:
            return True
