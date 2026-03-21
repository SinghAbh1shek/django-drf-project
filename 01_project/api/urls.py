from django.urls import path
from index.views import FormAPI

urlpatterns = [
    path('form/', FormAPI.as_view())
]
