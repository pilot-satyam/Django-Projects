from django.db.models.signals import post_save #post_save is used so that when user regiration is done, profile should be created auto.
from django.contrib.auth.models import User
from django.dispatch import receiver #reciever is required whenever the signals is used
from .models import profile

@receiver(post_save,sender=User) #receiver is here to receive the post_save signal and sender is the User,if signal is received then only this function will be called
def build_profile(sender,instance,created,**kwargs):
    if created: #if the instance is created
        profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()