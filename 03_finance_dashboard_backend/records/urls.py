from django.urls import path
from .views import RecordViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('records', RecordViewSet)
urlpatterns = [ ]
urlpatterns += router.urls