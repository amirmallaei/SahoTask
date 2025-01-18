from django.contrib import admin
from django.urls import path
from .views import UserActivityListView, LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),  # Landing page URL
    path("tracking/activity/", UserActivityListView.as_view(), name="activity"),
]

