# urls.py created by sylvi at 2020/12/24 10:51 AM
from django.conf.urls import url
from django.urls import path, include
# import social_django

from . import views

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    path('logout', views.logout),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]
