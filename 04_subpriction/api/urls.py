from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import BlogViewSet

router = DefaultRouter()
router.register('blogs', BlogViewSet)

urlpatterns = []

urlpatterns += router.urls
