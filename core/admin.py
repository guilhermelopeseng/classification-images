from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = ('image', 'predict', 'created_at', 'updated_at', 'is_activated')
