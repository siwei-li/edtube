# urls.py created by sylvi at 2021/5/4 10:01 PM

from django.conf.urls import url, include
# from django.urls import path
from rest_framework import routers

from .views import CommentsOp

router = routers.DefaultRouter()
router.register(r'(?P<video_id>[\d]+)/comments', CommentsOp,basename="comments")

urlpatterns = [
    url(r'^api/v1/videos/', include(router.urls), name='comments'),
]
