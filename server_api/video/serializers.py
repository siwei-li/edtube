# serializers.py created by sylvi at 2021/3/9 1:21 PM

from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'