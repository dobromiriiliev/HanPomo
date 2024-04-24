from django.db import models

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()

class PomodoroSession(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=25)  # Duration in minutes
    completed = models.BooleanField(default=False)
