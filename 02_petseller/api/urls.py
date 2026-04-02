from django.urls import path
from home.views import AnimalAPI

urlpatterns = [
    path('animals/', AnimalAPI.as_view()),
]
