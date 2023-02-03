from django.contrib import admin
from habit_tracker.models import ModelHabit
# Register your models here.

class HabitAdminConfig(admin.ModelAdmin):
    model=ModelHabit
    list_display=("id", "label", "periodicity", "begin_date", "end_date", "current_streak", "max_streak", "worst_streak", "completed")
admin.site.register(ModelHabit, HabitAdminConfig)
