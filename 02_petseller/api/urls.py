from django.urls import path
from home.views import AnimalAPI, AnimalDetailsView

urlpatterns = [
    path('animals/', AnimalAPI.as_view()),
    path('animal/<pk>/', AnimalDetailsView.as_view()),
]
