from django.urls import path
from users.views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
