from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


def create_profile(sender, created, instance, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)