# urls.py created by sylvi at 2020/12/24 10:51 AM
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('api/user_profile', views.update_profile),
    path('api/user_nickname', views.update_nickname),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]