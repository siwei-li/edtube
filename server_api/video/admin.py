from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','source']

admin.site.register(Video, VideoAdmin)