from django.test import TestCase
from habit_tracker.models import ModelHabit, ModelTask
import datetime as dt
from itertools import groupby


class TestClass(TestCase):

    def test_habit_model(self):
        model = ModelHabit.objects.create(label="Run", begin_date=dt.datetime.now(),
                                          end_date=dt.datetime.now())

        self.assertEquals("Run", str(model))

    def test_task_model(self):
        habit = ModelHabit.objects.create(label="Run twice", begin_date=dt.datetime.now(),
                                          end_date=dt.datetime.now())

        model = ModelTask.objects.create(done=True, task_date=dt.datetime.now(), habit=habit)

        self.assertEquals(True, model.done)

    def test_streak_number(self):

        habit = ModelHabit.objects.create(label="Run three times", begin_date=dt.datetime.now(),
                                          end_date=dt.datetime.now())

        ModelTask.objects.create(taskcomplete=True, task_date=dt.datetime.now(), habit=habit)
        ModelTask.objects.create(taskcomplete=True, task_date=dt.datetime.now(), habit=habit)
        ModelTask.objects.create(taskcomplete=True, task_date=dt.datetime.now(), habit=habit)

        habit = ModelHabit.objects.filter(id=habit.id)
        tasks = ModelTask.objects.filter(habit=habit[0])

        number_tasks = number_formatted(tasks)

        def best_streak(data) -> int:
            if number_tasks.__contains__(1):
                return max(len_iter(run) for val, run in groupby(data) if val)
            else:
                return 0

        max_streak = best_streak(number_tasks)

        self.assertEquals(3, max_streak)


def number_formatted(tasks):
    number_tasks = []

    for task in tasks:
        if task.done:
            number_tasks.append(1)
        else:
            number_tasks.append(0)
    return number_tasks


def len_iter(items):
    return sum(1 for _ in items)
