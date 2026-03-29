from django.urls import path
from index.views import FormAPI, QuestionAPI, ChoiceAPI

urlpatterns = [
    path('form/', FormAPI.as_view()),
    path('question/', QuestionAPI.as_view()),
    path('choices/', ChoiceAPI.as_view()),
]
