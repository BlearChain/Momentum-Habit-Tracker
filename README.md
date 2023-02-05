# Momentum-Habit-Tracker
OoO with Python and Django for IU Project portafolio

# Setup

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.
I used Anaconda that is an open-source distribution of the Python and R programming languages for data science that aims to simplify package management and deployment. you can download it from [this link](https://www.anaconda.com/products/distribution) as it created this virtualenv for you.

Here are the steps for regular use without a virtualenv:

Initially you must clone this repository:

```sh
git clone https://github.com/BlearChain/Momentum-Habit-Tracker.git

```

to use the app, you must install `Pyhton` ver 3.10 or superior.
you can install it via pip or you can download the latest version of Python from [this link.](https://www.python.org/downloads/) - Make sure to check "ADD to path" in the Python installer. 
```sh
pip install python
```
Once `pip` has finished downloading the dependencies:

```sh
cd Momentum-Habit-Tracker
python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/show_habits`.

## Momentum Habit Tracker's Core Functionality
The Momentum habit tracker web app basically allows you to:
* View you current habits (5 can be preloaded as predefined ones)
* Add a new habit
* Delete a current habit in the app
* Define and edit the periodicity of habits (Daily, weekly, and monthly)
* Mark your habit and its tasks as completed

### Habit/Task Streak Tracker
the Momentun App lets you view the following information:
* View the current, best and worst streaks of all habits

#### Usage
Once you navigate to http://127.0.0.1:8000/show_habits the main page looks like this:

![Main_page](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/View%20all%20habits.jpg?raw=true)

Here you can view all your current habits and the availbale information on them (in this example, there are 5 preladed habits on display)

If you wish to create a new habit, you can simply click on `Create A New Habit` button:
Here is an screenshot of the create a habit page looks like:

![Create a new habit](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/Create%20a%20new%20habit.jpg?raw=true)

and you can complete the new habit creation process by clicking on the `Create habit` button.

To complete your tasks, you need to click on the `Show tasks` button that each habit has on the habits screen. This leads you to another screen where you can see all the current tasks that you have for this current habit in accordance to the selected periodicity for that habit. and if this task has been completed or not bt tw means: uno with a False or True test in the Done column and a check mark, that does confirm if the task is completed or not.

![tasks](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/Tasks.jpg?raw=true)

to complete a task, you must click on the `Complete Task` button you see next to each task, this will lead you to the following screen:
 
![task complete](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/complete%20task.jpg?raw=true)

Here you can check to complete de task in hand!

To see your current streaks for any of your habits, you have to click on the `My Habits Streaks` button. this will bring anotehr page where you can see this information:

![Streaks](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/Habit%20Streaks.jpg?raw=true)

On this last pagem, you can see the current, best and worst streak you have for any of your current habits up to today.


