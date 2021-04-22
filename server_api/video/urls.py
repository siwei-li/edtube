# urls.py created by sylvi at 2021/3/9 1:12 PM
from django.urls import path

from . import views

urlpatterns = [
    path('api/videos/public', views.getVideoList),
    path('api/videos/<int:id>', views.getVideo),

]