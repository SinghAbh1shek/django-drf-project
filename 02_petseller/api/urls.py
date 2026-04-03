from django.urls import path
from home.views import AnimalAPI, AnimalDetailsView, RegisterAPI, LoginAPI

urlpatterns = [
    path('animals/', AnimalAPI.as_view()),
    path('animal/<pk>/', AnimalDetailsView.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
