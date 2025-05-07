from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, OTP, BankCard

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ("phone", "first_name", "last_name", "is_profile_completed", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("phone", "first_name", "last_name")
    ordering = ("phone",)

    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Custom", {"fields": ("is_profile_completed",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OTP)
admin.site.register(BankCard)
