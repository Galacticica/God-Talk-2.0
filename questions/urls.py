from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_page"),
    path('ask/', views.ask_question_view, name='ask_question_page'), 
    path('ask/<int:parent_id>/', views.ask_question_view, name='ask_question_page'),  
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]