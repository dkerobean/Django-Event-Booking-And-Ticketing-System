from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name,
            email=user.email
        )


def deleteUser(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
