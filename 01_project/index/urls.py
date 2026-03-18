from django.urls import path
from .views import TestAPI
urlpatterns = [
    path('api/test/', TestAPI.as_view()),
]
