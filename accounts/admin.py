from django.contrib import admin

# Register your models here.
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "license_expiry_date",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name", "license_expiry_date", "hdd")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name", "license_expiry_date", "hdd")}),
    )
    readonly_fields = ('hdd',)  # Hace que el campo 'hdd' sea de solo lectura

admin.site.register(CustomUser, CustomUserAdmin)    