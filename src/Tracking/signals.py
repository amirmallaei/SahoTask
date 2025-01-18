from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, UserActivity
from django.contrib.auth.models import User

@receiver(user_logged_in)
def log_user_login(user, **kwargs):
    UserActivity.objects.create(user=user, action='login')

@receiver(user_logged_out)
def log_user_logout(user, **kwargs):
    UserActivity.objects.create(user=user, action='logout')

@receiver(post_save, sender=User)
def log_profile_update(instance, created, **kwargs):
    if not created:
        UserActivity.objects.create(user=instance, action='update_profile')

@receiver(post_save, sender=Post)
def post_created(instance, created, **kwargs):
    if created:
        UserActivity.objects.create(user=instance.author, action='create_post')
   

