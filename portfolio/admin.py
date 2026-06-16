from django.contrib import admin
from .models import ContactMessage, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'accent_color', 'order', 'is_visible', 'created_at')
    list_editable = ('order', 'is_visible', 'accent_color')
    list_filter = ('is_visible', 'accent_color')
    search_fields = ('title', 'description', 'tech_stack')
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'description', 'tech_stack', 'image')  # image add kiya
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Display Settings', {
            'fields': ('accent_color', 'order', 'is_visible')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at', 'ip_address')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at', 'ip_address')
    list_editable = ('status',)
    ordering = ('-created_at',)
    fieldsets = (
        ('Sender Info', {
            'fields': ('name', 'email', 'ip_address')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Meta', {
            'fields': ('status', 'created_at')
        }),
    )