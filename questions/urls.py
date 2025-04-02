from django.urls import path
from .views import HomeView, ask_question_view

urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path("ask/", ask_question_view, name="ask_question_page"),
]