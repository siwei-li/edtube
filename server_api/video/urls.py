# urls.py created by sylvi at 2021/3/9 1:12 PM

# from django.urls import path
# from drf_yasg.inspectors import view
from django.conf.urls import url, include
from rest_framework import routers

from .views import VideosOp
# from . import views

router = routers.DefaultRouter()
router.register(r'videos', VideosOp)

urlpatterns = [
    # path('api/v1/videos/', views.get_post_videos, name="get_post_videos"),
    # path('api/v1/videos', views.VideosOp.as_view(), name="get_post_videos"),
    url(r'^api/v1/', include(router.urls),name="videos"),
    # path('api/v1/videos/<int:id>', views.get_delete_update_video, name="get_delete_update_video"),
    # path('api/v1/videos/search',views.reverse())
]