from django.contrib import admin
from .models import photos

# Register your models here.

class photos_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'url',
        'photo',
        'photo_slug',
    )
admin.site.register(photos, photos_admin)
