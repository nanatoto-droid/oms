from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, Profile

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Extra', {'fields': ('start_date',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename', 'content_type')
    list_filter = ('content_type',)
    search_fields = ('name', 'codename')