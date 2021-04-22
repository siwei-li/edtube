from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from video.models import Video
from video.serializers import VideoSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def getVideoList(request):
    # TODO generate user specific list
    videos = Video.objects.all()
    videoSerializer = VideoSerializer(videos, many=True)
    return JsonResponse(videoSerializer.data,safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def getVideo(request,id):
    video = Video.objects.get(id=id)
    videoSerializer = VideoSerializer(video)
    return JsonResponse({"data":videoSerializer.data})
