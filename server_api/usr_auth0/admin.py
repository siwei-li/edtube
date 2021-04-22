from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','auth0_user']

admin.site.register(Profile,ProfileAdmin)
