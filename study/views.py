from django.shortcuts import render
from .models import Flashcard, PomodoroSession

def index(request):
    return render(request, 'study/index.html')

def flashcard_view(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'study/flashcards.html', {'flashcards': flashcards})

def pomodoro_view(request):
    if request.method == "POST":
        # Start a new Pomodoro session
        PomodoroSession.objects.create()
        return render(request, 'study/pomodoro.html', {'session_started': True})
    return render(request, 'study/pomodoro.html', {'session_started': False})
