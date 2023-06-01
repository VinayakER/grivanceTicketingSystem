from django.contrib import admin
from .models import User, Department
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _


class User_Creation_Form(UserCreationForm):  
    class Meta:
        model = User 
        fields = "__all__"

from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','department')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff','is_admin','is_student', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'department','is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups','department')
class User_Admin(CustomUserAdmin):
    model = User
    add_form = User_Creation_Form

admin.site.register(User, User_Admin)
admin.site.register(Department)

# Register your models here.
