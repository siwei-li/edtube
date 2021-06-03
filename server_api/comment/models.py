from django.db import models
from video.models import Video
from django.contrib.auth.models import User

from rest_framework import serializers


# Create your models here.
class Comment(models.Model):
    video_id = models.ForeignKey(Video,on_delete=models.CASCADE)
    parent = models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    # user_id = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,to_field="username",db_column="user_id")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    message = models.TextField(max_length=5000,blank=False)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def nickname(self):


    @property
    def replies(self):
        reply_serializer= ReplySerializer(Comment.objects.filter(parent=self),many=True)
        return reply_serializer.data

    def __str__(self):
        return f"Comment {self.id} on {self.video_id}: {self.message}"

    class Meta:
        db_table = 'comments'
        ordering = ['created_at']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_id', 'message', 'likes','created_at']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user_id', 'message', 'likes','created_at','replies']


