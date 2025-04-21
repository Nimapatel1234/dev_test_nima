from django.contrib import admin
from .models import StaffUser

@admin.register(StaffUser)
class StaffUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_admin', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_admin', 'is_active']
    search_fields = ['name', 'email']
