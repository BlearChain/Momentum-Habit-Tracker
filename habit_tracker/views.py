from itertools import groupby
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from habit_tracker.forms import FormHabit
from habit_tracker.models import ModelTask, ModelHabit
from django.views import View
import datetime as dt
from datetime import date, datetime
from django.views.generic.edit import DeleteView, UpdateView
import json
from django.conf import settings
import os

# Create your views here.

class Index(View):
    """
    This is a Class to just define the main menu Index and return render of tracking_main.html
    """
    def get(self, request):
        return render(request, "tracking_main.html",{})

class CreateCommonHabit(View):
    """
    This is a class to load predefined habits to the habit App
    """
    def get(self, request):
        form = FormHabit()
        return render(request, "create-common.html", {"form": form})
    def post(self, request):
        json_data = os.path.join(settings.BASE_DIR, 'static', "habit_common.json")
        
        with open(json_data, 'r') as f:
            data = json.load(f)
            for habit in data:
                
                data_create = {
                    "label": habit["label"],
                    "periodicity": habit["periodicity"],
                    "begin_date": date.today(),
                    # "end_date": date.today() + 30
                }
                print(data_create)
        return redirect('/show_habits')        

class CreateHabit(View):
    """
    This class is a view that is used to create a habit. 
    It defines a get method which takes in a request and creates an instance 
    of the FormHabit class. It then renders the create_a_habit.html page with the 
    form as an argument.
    """
    def get(self, request):
        form = FormHabit()
        return render(request, "create_a_habit.html", {"form": form})

    def post(self, request):
        data = request.POST
        habit_exists = ModelHabit.objects.filter(label=data.get("label")).exists()
        #checks if habit already exists in db if it does exist redirects back to home page 
        if habit_exists:
            return redirect('/')
        begin_date = data.get('begin_date') #gets start date from form data 
        end_date = data.get('end_date') #gets end date from form data
        period = data.get('periodicity') #gets periodicity from form data
                
        habit_model = FormHabit(data) #creates instance of FormHabit with form data 
        step = None #sets step to None initially 
        if period == "DAILY":
            step = dt.timedelta(days=1)
        elif period == "WEEKLY":
            step = dt.timedelta(days=7)
        elif period == "MONTHLY":
            step = dt.timedelta(days=30)
        if habit_model.is_valid(): #validates model before saving to db 
            if end_date < begin_date:
                return HttpResponseBadRequest("Error: Habit End date must be after Begin date")
            habit = habit_model.save()
            saved_habit = ModelHabit.objects.filter(label=habit)
            formated_begin_date = dt.datetime.strptime(begin_date, "%Y-%m-%d").date()
            formated_end_date = dt.datetime.strptime(end_date, "%Y-%m-%d").date()
            while formated_begin_date <= formated_end_date:
                date = formated_begin_date.strftime("%Y-%m-%d")
                task = ModelTask(taskcomplete=False, task_date=date, habit=saved_habit[0])
                task.save() #saves model to db
                formated_begin_date += step
        return redirect('/show_habits')

class View_All_Habits(View):
    """
    This class is a subclass of the View class and is used to view all habits. 
    It defines a get() method which retrieves all the habits from the ModelHabit object, as well as their ids. 
    It then uses the ids to count how many tasks are associated with each habit, and stores this information in a context dictionary. 
    Finally, it renders the tracking_main.html template with the context dictionary as an argument.
    """
    def get(self, request):
        habits = ModelHabit.objects.values()
        
        habits_ids = ModelHabit.objects.values_list("id")
        for item in habits_ids:
            count_habits = ModelTask.objects.filter(habit=item).count()
        context = {'habits': habits}
        return render(request, 'tracking_main.html',context)

class DeleteHabit(DeleteView):
    """
    This class is a DeleteView class which is used to delete a ModelHabit object.
    The success_url attribute specifies the URL to which the user should be redirected 
    after deleting the ModelHabit object.

    """
    model = ModelHabit
    success_url = "/show_habits"

class UpdateHabit(UpdateView):
    """
    This class is a subclass of UpdateView and is used to update a ModelHabit object.
    It uses the template "Model_Habit_form.html" to render the form for updating the ModelHabit object. 
    The fields that can be updated are begin_date, end_date, periodicity, and completed. 
    After the form is submitted, the user will be redirected to the '/show_habits' page.

    """
    model = ModelHabit
    template_name = "Model_Habit_form.html"
    fields = ["begin_date","end_date","periodicity","completed"]
    success_url = '/show_habits'


class Monthly_Habits(View):
    """
    This a class called Monthly_Habits that inherits from the View class.
    The get method of this class filters all ModelHabit objects with a periodicity of "MONTHLY" 
    and stores them in the variable habits. 
    The request and the filtered habits are then passed to the render function which renders the 'tracking_main.html'
    template with the given context.

    """
    def get(self, request):
        habits = ModelHabit.objects.filter(periodicity="MONTHLY")
        context = {'habits': habits}
        return render(request, 'tracking_main.html', context)

class Weekly_Habits(View):
    """
    This is a class called Weekly_Habits that inherits from the View class. 
    It has a get method which filters ModelHabit objects for those with a periodicity of "WEEKLY".
    It then creates a context dictionary containing the filtered habits and renders the trackin_gmain.html
    template with the context dictionary as an argument.
    """
    def get(self, request):
        habits = ModelHabit.objects.filter(periodicity="WEEKLY")
        context = {'habits': habits}
        return render(request, 'tracking_main.html', context)

class Daily_Habits(View):
    """
    This  is a class named Daily_Habits that inherits from the View class.
    The get method of this class filters ModelHabit objects with the periodicity "DAILY" 
    and stores them in the habits variable.
    It then creates a context dictionary with the habits variable and renders the trackingmain.html
    template with this context.

    """
    def get(self, request):
        habits = ModelHabit.objects.filter(periodicity="DAILY")
        context = {'habits': habits}
        return render(request, 'tracking_main.html', context)

class TasksView(View):
    """
    This class is a view for the ModelTask model.
    It defines a get method that takes in a request and a primary key (pk) as parameters.
    The method filters the ModelTask objects based on the given pk and stores them in the tasks variable.
    It then creates a context dictionary with the tasks variable and passes it to the render function 
    along with the request and tasks.html template to render the response.
    """
    model = ModelTask
    def get(self, request, pk):
        tasks = ModelTask.objects.filter(habit=pk)
        context = {'tasks': tasks}
        return render(request, 'tasks.html', context)


class Update_Task(UpdateView):
    """
    This class is a subclass of UpdateView and is used to update the ModelTask model.
    The template used for the form is called "Model_Task_form.html" and it will only have one field, "taskcomplete".
    After the action in form is submitted, the user will be redirected to the '/show_habits' page.
    """
    model = ModelTask
    template_name = "Model_Task_form.html"
    fields = ["taskcomplete"]
    success_url = '/show_habits'


class All_Streaks(View):
    """
    This class defines a view called All_Streaks. 
    It contains a get() method which retrieves all habits from the ModelHabit database,
    creates an empty list for habit streaks, and initializes a counter for the worst streak to 0.
    It then sets the current date as a string in the format '%Y-%m-%d'. 
    For each habit in habits, it retrieves all tasks from the ModelTask database associated with that habit
    and creates an empty list for amount of tasks. 
    Depending on the periodicity of the habit, it sets a step variable as either one day, one week or one month.
    It then iterates through each task in tasks and formats its date as a string in the format '%Y-%m-%d'.
    If this formatted date is earlier than or equal to the current date, it checks if the task is complete and adds 1 to amount_tasks 
    if it is or 0 if it isn't. The datetask variable is then incremented by step depending on periodicity. 
    For each item in amounttasks, if it is 1 (the task was completed), it increments habit's current streak by 1 
    and checks if this value is greater than or equal to its max streak; if so, max streak is set to current streak.
    The counter for worst streak is reset to 0. If item is 0 (the task was not completed), counter for worst streak 
    is incremented by 1 and checked against habit's worst streak; if greater than worst streak, worst streak is set to counter's
    value and current streak set back to 0. The updated habit object is saved and appended to habitstreaks list. 
    Finally, context dictionary containing Habitstreaks list is passed into AllStreaks template which renders
    all streaks associated with each habit in HTML format.
    """
    def get(self, request):
        habits = ModelHabit.objects.all()
        habit_streaks = []
        counter_worst_streak = 0 #reset worst streak counter to 0
        now = datetime.now() #define date as today
        current_date = now.strftime('%Y-%m-%d')   #format date to YYYY-MM-DD format
        for habit in habits:
            tasks = ModelTask.objects.filter(habit=habit)  
            amount_tasks = []
            step = None
            habit.current_streak=0 #set current streak to 0
            habit.max_streak=0 #set current streak to 0
            habit.worst_streak=0 #set current streak to 0
            if habit.periodicity == "DAILY": #see if periodicity is daily define delta
               step = dt.timedelta(days=1)
            elif habit.periodicity == "WEEKLY": #see if periodicity is weekly define delta
               step = dt.timedelta(days=7)
            elif habit.periodicity == "MONTHLY": #see if periodicity is monthly define delta
                step = dt.timedelta(days=30)
            for task in tasks:
                datetask= task.task_date
                formated_datetask = dt.datetime.strftime(datetask,'%Y-%m-%d')
                if current_date >= formated_datetask: #compare Task_date with current_date for task streak validation up to date
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
            habit.save()
            habit_streaks.append(habit)
        context= {'Habit_streaks': habit_streaks}
        return render(request, 'All_Streaks.html',context)



class Task_Streaks(View):
    """
    This class defines a view for calculating the maximum task streak for a given habit. It contains four methods: 
    formatedtasks() - takes in a list of tasks and returns a list of 1s and 0s based on whether the task is complete or not. 
    amounttasks() - takes in an iterable item and returns the sum of all items in it. 
    get() - takes in a request and primary key (pk) for the habit, filters out all tasks associated with that habit,
    formats them using formatedtasks(), calculates the maximum streak using beststreak(),
    and renders it to the streak.html template with context containing maxstreak. 
    beststreak() - takes in data and returns the maximum number of consecutive tasks if there are any completed tasks
    that are dated today or earlier. Otherwise, it returns 0.

    """
    def formated_tasks(self, tasks):
        number_of_tasks = []   
        for task in tasks:
            if task.taskcomplete:
                number_of_tasks.append(1)
            else:
                number_of_tasks.append(0)
        return number_of_tasks,
    def amount_tasks(self, items):
        return sum(1 for _ in items)
    def get(self, request, pk):
        habit = ModelHabit.objects.filter(id=pk)
        tasks = ModelTask.objects.filter(habit=habit[0])  
        number_tasks = self.formated_tasks(tasks)
        def best_streak(data) -> int:
             if number_tasks.__contains__(1) and tasks.task_date <= date.today():
                return max(self.amount_tasks(run) for val, run in groupby(data) if val)
             else:
                 0
        max_streak = best_streak(number_tasks)
        print(max_streak)
        context={'max_streak': max_streak}
        return render(request, 'streak.html', context)
