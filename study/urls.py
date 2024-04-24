from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flashcards/', views.flashcard_view, name='flashcards'),
    path('pomodoro/', views.pomodoro_view, name='pomodoro'),
]
