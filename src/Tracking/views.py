from django.shortcuts import render
from django.views.generic import ListView
from .models import UserActivity

class UserActivityListView(ListView):
    """Log User Activities HTML Page"""
    model = UserActivity
    template_name = 'user_activities.html'
    context_object_name = 'activities'
    paginate_by = 10  
    
    def get_queryset(self):
        activities = UserActivity.objects.all().order_by('-timestamp')
        return activities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
