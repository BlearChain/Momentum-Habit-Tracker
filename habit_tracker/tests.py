from habit_tracker.models import ModelHabit, ModelTask
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
                                          end_date='2023-02-30')

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
        tasks = ModelTask.objects.filter(habit=habit[0])
        tasks = ModelTask.objects.filter(habit=habit)  
        testdate="2023-02-07"
        amount_tasks = []
        step = dt.timedelta(days=1)
        for task in tasks:
            datetask= task.task_date
            formated_datetask = dt.datetime.strftime(datetask,'%Y-%m-%d')
            if testdate >= formated_datetask: 
                if task.taskcomplete:
                    amount_tasks.append(1)
                    datetask += step
                else:
                    amount_tasks.append(0)
                    datetask += step    
                for item_amount in amount_tasks:
                    if item_amount == 1:
                        habit.current_streak += 1
                        if habit.current_streak >= habit.max_streak:
                            habit.max_streak = habit.current_streak                
                        counter_worst_streak = 0
                    else:
                        counter_worst_streak += 1
                        if counter_worst_streak > habit.worst_streak:
                            habit.worst_streak = counter_worst_streak
                        habit.current_streak = 0
        
        max_streak = habit.max_streak
        worst_streak=habit.worst_streak

        self.assertEquals(4, max_streak)
        self.assertEquals(3, worst_streak)

  
class TrackingRecordModelTestCase(unittest.TestCase):
    def setUp(self):
        habit = ModelHabit.objects.create(label='Meditate')
        habit.objects.create(habit=habit, begin_date='2023-01-01')
        habit.objects.create(habit=habit, end_date='2023-01-02')

    def test_records_are_created(self):
        habit = ModelHabit.objects.get(label='Meditate')
        record1 = ModelTask.objects.get(habit=habit, task_date='2023-01-01')
        record2 = ModelTask.objects.get(habit=habit, task_date='2023-01-02')
        self.assertEqual(record1.habit, habit)
        self.assertEqual(record2.habit, habit)
