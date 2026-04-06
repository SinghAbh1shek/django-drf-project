from django.urls import path
from .views import RegisterAPI, LoginAPI, ListUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', ListUserViewSet)

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]

urlpatterns += router.urls