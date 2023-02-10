from habit_tracker.models import ModelHabit, ModelTask
from habit_tracker.views import All_Streaks
import datetime as dt
import unittest
from django.test import Client



class TestClass(unittest.TestCase):

    def test_model_habit(self):
        model = ModelHabit.objects.create(label="Run 10km a week", begin_date='2023-01-01',
                                          end_date='2023-03-01')

        self.assertEquals("Run 10km a week", str(model))

    def test_model_task(self):
        habit = ModelHabit.objects.create(label="Run twice", periodicity='DAILY', begin_date='2023-02-01',
                                          end_date='2023-02-10')

        model = ModelTask.objects.create(taskcomplete=True, task_date='2023-02-07', habit=habit)

        self.assertEquals(True, model.taskcomplete)

    def test_streak(self):

        habit = ModelHabit.objects.create(label="Drink more water", periodicity='DAILY', begin_date='2023-02-01',
                                          end_date='2023-02-20' )

        ModelTask.objects.create(taskcomplete=True, task_date='2023-02-01', habit=habit)
        ModelTask.objects.create(taskcomplete=True, task_date='2023-02-02', habit=habit)
        ModelTask.objects.create(taskcomplete=True, task_date='2023-02-03', habit=habit)
        ModelTask.objects.create(taskcomplete=True, task_date='2023-02-04', habit=habit)

        habit = ModelHabit.objects.filter(id=habit.id)
        # tasks = ModelTask.objects.filter(habit=habit[0])
        tasks = ModelTask.objects.filter(habit=habit)  
        All_Streaks=All_Streaks.get()
        self.assertEquals(4, All_Streaks.max_streak)
        self.assertEquals(5, All_Streaks.worst_streak)

  
class TrackingRecordModelTestCase(unittest.TestCase):
     def setUp(self):
         habit = ModelHabit.objects.create(label='Meditate', begin_date='2023-01-01', end_date='2023-01-02')


     def test_records_are_created(self):
         habit = ModelHabit.objects.filter(id=habit.id)
         model = ModelTask.objects.filter(label='Meditate')
         record1 = ModelTask.objects.filter(habit=habit, task_date='2023-01-01')
         record2 = ModelTask.objects.filter(habit=habit, task_date='2023-01-02')
         self.assertEqual(record1.habit, habit)
         self.assertEqual(record2.habit, habit)




