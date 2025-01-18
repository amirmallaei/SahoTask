from django.contrib import admin
from .models import UserActivity, Post

# Register your models here.
admin.site.register(UserActivity)
admin.site.register(Post)