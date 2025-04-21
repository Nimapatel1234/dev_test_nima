from django.contrib import admin
from .models import Ticket, Attachment

class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'assigned_to', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['name', 'description']
    inlines = [AttachmentInline]

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'file', 'uploaded_at']

