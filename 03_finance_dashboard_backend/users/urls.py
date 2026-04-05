from django.urls import path
from .views import RegisterAPI, LoginAPI, UpdateUserRoleAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('update-user-role/', UpdateUserRoleAPI.as_view()),
]
