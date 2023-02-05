# Momentum-Habit-Tracker
OoO with Python and Django for IU Project portafolio

# Setup

Initially you must clone this repository:

```sh
git clone https://github.com/BlearChain/Momentum-Habit-Tracker.git
cd "to the folder where it was stored"
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

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

## Habit Tracker's Core Functionality
The Momentum habit tracker web app basically allows you to:
* View you current habits (5 can be preloaded as predefined ones)
* Add a new habit 
* Delete a current habit in the app
* Define and edit the periodicity of habits (Daily, weekly, and monthly)
* Mark your habit ans its tasks as completed

### Progress and Streak Tracker
Additionally, the user can view:
* View all of their current habits
* View all the habits for a specific period (Monthly, Weekly or Daily)
* View the current, best and worst streaks of all habits



