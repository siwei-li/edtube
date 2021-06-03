from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','video_id', 'user_id', 'message', 'likes','created_at']

admin.site.register(Comment,CommentAdmin)
