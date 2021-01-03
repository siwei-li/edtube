# serializers.py created by sylvi at 2020/12/31 1:59 PM

from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
                  'bio',
                  'birth_date',
                  'gender')
        # fields = '__all__'

class NicknameSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=30)

