from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    auth0_user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    # location = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'profile'  # 指明数据库表名

    def __str__(self):
        return "Profile of user " + str(self.auth0_user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(auth0_user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class Auth0Meta(models.Model):
#     nickname = models.CharField(max_length=30)
#     user_avatar_url = models.URLField(max_length=200)
#
#     class Meta:
#         db_table = 'auth_user_meta'  # 指明数据库表名
#
#     def __str__(self):
#         return "Auth0 meta data of " + self.auth0_user