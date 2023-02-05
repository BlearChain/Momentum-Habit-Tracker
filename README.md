# Momentum-Habit-Tracker
OoO with Python and Django for IU Project portafolio

# Setup

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.
I used Anaconda that is an open-source distribution of the Python and R programming languages for data science that aims to simplify package management and deployment. you can download it from [this link](https://www.anaconda.com/products/distribution) as it created this virtualenv for you.


Here are the steps for regular use without a virtualenv:

Initially you must clone this repository:

```sh
git clone https://github.com/BlearChain/Momentum-Habit-Tracker.git
cd Momentum-Habit-Tracker
```

to use the app, you must install Pyhton ver 3.10 or superior.
you can install it via pip 
```sh
pip install python
```
You can download the latest version of Python from [this link.](https://www.python.org/downloads/) - Make sure to check "ADD to path" in the Python installer. 

Once `pip` has finished downloading the dependencies:
```sh
cd project
python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/show_habits`.

![Main_page](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/View%20all%20habits.jpg?raw=true)

## Mmomentum Habit Tracker's Core Functionality
The Momentum habit tracker web app basically allows you to:
* View you current habits (5 can be preloaded as predefined ones)
* Add a new habit
* Delete a current habit in the app
* Define and edit the periodicity of habits (Daily, weekly, and monthly)
* 
![Create a new habit](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/Create%20a%20new%20habit.jpg?raw=true)

* Mark your habit and its tasks as completed

![task complete](https://github.com/BlearChain/Momentum-Habit-Tracker/blob/main/__screenshots/complete%20task.jpg?raw=true)

### Task Streak Tracker
here you can view the following information:
* View all of current habits streaks
* View all the streaks for a specific period (Monthly, Weekly or Daily)
* View the current, best and worst streaks of all habits



