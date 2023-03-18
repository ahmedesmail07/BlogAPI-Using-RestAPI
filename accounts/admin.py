from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("name", "email", "username", "phone_number", "is_staff")
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", "phone_number")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name", "phone_number")}),
    )


# class CustomUserAdminView(admin.ModelAdmin):
#     list_display = ("name", "phone_number")


admin.site.register(CustomUser, CustomUserAdmin)
