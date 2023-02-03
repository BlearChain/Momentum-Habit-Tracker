from django.db import models
from model_utils import Choices
from datetime import date, datetime
import pandas as pd

# Create your models here.

class ModelHabit(models.Model):
    """
    Model for a Habit entry
    """
    class Meta:
        db_table = "habit"
    DURATION = Choices("DAILY", "WEEKLY", "MONTHLY")
    label = models.CharField(max_length=200)
    periodicity = models.CharField(max_length=10, choices=DURATION, default=DURATION.DAILY)
    creation_date= models.DateField(auto_now=True)
    begin_date = models.DateField()
    end_date = models.DateField()
    current_streak = models.IntegerField(default="0")
    max_streak = models.IntegerField(default="0")
    worst_streak = models.IntegerField(default="0")
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.label

class ModelTask(models.Model):
    """
    Model for a Task entry, related to  Habit model
    """
    class Meta:
        db_table = "task"
    taskcomplete = models.BooleanField(default=False)
    task_date = models.DateField()
    habit = models.ForeignKey(ModelHabit, related_name="habit_task", on_delete=models.CASCADE)
    def __str__(self):
        return self.habit.label

