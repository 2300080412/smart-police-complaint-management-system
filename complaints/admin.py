from django.contrib import admin
from django.utils.html import format_html
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = [
    'id',
    'name',
    'mobile',
    'complaint_type',
    'status',
    'latitude',
    'longitude',
    'image_preview'
]

    search_fields = [
        'name',
        'mobile',
        'complaint_type'
    ]

    readonly_fields = ['full_image']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Evidence"

    def full_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="400" style="border-radius:10px;" />',
                obj.image.url
            )
        return "No Image"

    full_image.short_description = "Uploaded Evidence"