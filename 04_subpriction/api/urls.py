from django.urls import path
from home.views import TestAPI
urlpatterns = [
    path('test/', TestAPI.as_view())
]
