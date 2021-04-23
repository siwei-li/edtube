# test_video.py created by sylvi at 2021/4/23 9:37 AM
from django.test import TestCase, Client
from .models import Video
from .serializers import VideoSerializer

# initialize the APIClient app
client = Client()

class VideoTestCase(TestCase):
    # def setUp(self):
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    def test_getVideo(self,id=2):
        video = Video.objects.get(id=id)
        self.assertEqual(video.title, 'Effective Ways to Practice Arpeggios')
