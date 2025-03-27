from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the CustomUser model
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'is_active'
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_photo',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)