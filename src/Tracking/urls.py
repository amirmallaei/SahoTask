from django.contrib import admin
from django.urls import path
from .views import UserActivityListView

urlpatterns = [
    path("activity/", UserActivityListView.as_view(), name="activity"),
]

