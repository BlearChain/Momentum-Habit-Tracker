from .views import CreateHabit, CreateCommonHabit, DeleteHabit, UpdateHabit, View_All_Habits, Monthly_Habits, Weekly_Habits, Daily_Habits, TasksView, Update_Task, Task_Streaks, All_Streaks, Index
from django.urls import path



urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('delete/<pk>', DeleteHabit.as_view(),),
    path('update/<pk>', UpdateHabit.as_view(), name='update'),
    path('show_habits', View_All_Habits.as_view(), name='show_habits'),
    path('monthly_habits', Monthly_Habits.as_view(), name='monthly_habits'),
    path('weekly_habits', Weekly_Habits.as_view(), name='weekly_habits'),
    path('daily_habits', Daily_Habits.as_view(), name='daily_habits'), 
    path('show_tasks/<pk>', TasksView.as_view(), name='show_tasks'),
    path('update_task/<pk>', Update_Task.as_view(), name='update_task'),
    path('Task_streak/<pk>', Task_Streaks.as_view(), name='streak'),
    path('All_Streaks', All_Streaks.as_view(), name='All_Streaks'),
    path('create_a_habit', CreateHabit.as_view(), name='create_a_habit'),
    path("create-common", CreateCommonHabit.as_view(), name="create-common")
]