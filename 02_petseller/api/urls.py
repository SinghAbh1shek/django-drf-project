from django.urls import path
from home.views import test

urlpatterns = [
    path('test/', test),
]
