from django.urls import path
from .views import DashboardAPI

urlpatterns = [
    path('', DashboardAPI.as_view()),
]
