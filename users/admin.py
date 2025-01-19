from django.contrib import admin
from .models import CustomUser, VerificationCode, Role, UserRole


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'mobile',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'is_mobile_verified',
    )


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'uuid',
        'created_at',
        'verification_code',
        'is_valid',
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    pass
