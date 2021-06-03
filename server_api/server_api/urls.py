"""server_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="EdTube API",
        url='/v1',
        default_version='v1',
        description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="siwei.li@live.com"),
        # license=openapi.License(name="BSD License"),
        validators=['ssv'],
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = "EdTube Admin"
admin.site.site_title = "EdTube Admin Portal"
admin.site.index_title = "Welcome to EdTube Portal"

urlpatterns = [
    path('api/v1/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('admin-edtube/', admin.site.urls, name="admin"),
    path('', include('usr_auth0.urls')),
    path('', include('video.urls')),
    path('', include('comment.urls')),
]
