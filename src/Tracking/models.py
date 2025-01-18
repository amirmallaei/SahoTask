from django.contrib.auth.models import User
from django.db import models

class UserActivity(models.Model):
    ACTION_CHOICES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('create_post', 'Create Post'),
        ('update_profile', 'Update Profile'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, verbose_name='ACTION')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='DATE and TIME')

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"