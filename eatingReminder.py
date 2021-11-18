'''
me aisa program bana araha hu ki jo aapko khana khane ka yaad dilaye at a certain time but iske liye apne ko pahile datetime module ko import karna padega and then woh module sey present time ko access karenege 
and fir present time eating time ko compare karenege and agar eating time == present time then fir reminder ka function chalu hoga
'''
import time
import datetime
from types import SimpleNamespace
from plyer import notification

''' creating function here for reminding for dinner ,breakfast ,lunch,chai,har 3 hr me kuch na kuch khane ko '''
# lets create a function for breakfast

def itsBreakfastTime():
    
    while True:
        notification.notify(
            title = 'Breakfast reminder',
            message = '''A healthy breakfast has many health benefits, so try not to skip it.
                ''',
            app_icon = "E:\\Python\\AutomatePython\\reminders\\eatSomeThing\\breakfast.ico",
            timeout = 10
        )

# lets create a function for lunch
def itsLunchTime():
    
    while True:
        notification.notify(
            title = 'lunch time reminder',
            message = '''According to experts, lunch provides nourishment to the body and brain and reduces stress and eating lunch provides a break from the activities of the day and gives energy for the rest of the afternoon
                ''',
            app_icon = "E:\\Python\\AutomatePython\\reminders\\eatSomeThing\\breakfast.ico",
            timeout = 10
        )

# lets create function for dinner
def itsTimeForDinner():

    while True:
        notification.notify(
            title = 'Dinner reminder',
            message = '''Dinners keep kids healthy – A warm receptive atmosphere at mealtime does a lot for kids' health. They tend to eat more fruits and vegetables, have less problems with issues such as asthma, and avoid obesity
            ''',

            app_icon = "E:\\Python\\AutomatePython\\reminders\\eatSomeThing\\breakfast.ico",
            timeout = 10
        )
getPresentTime = datetime.datetime.now()
print(getPresentTime)

def check():
    while True:
        notification.notify(
            title = 'Dinner reminder',
            message = '''Dinners keep kids healthy – A warm receptive atmosphere at mealtime does a lot for kids' health. They tend to eat more fruits and vegetables, have less problems with issues such as asthma, and avoid obesity
            ''',

            app_icon = "E:\\Python\\AutomatePython\\reminders\\eatSomeThing\\breakfast.ico",
            timeout = 10
        )

getHour = int(getPresentTime.strftime('%H'))
getMinutes = int(getPresentTime.strftime('%M'))

if __name__ == '__main__':
    while True:
        if getHour == 11 and getMinutes == 30:
            itsBreakfastTime()

        if getHour == 14 and getMinutes == 40:
            itsLunchTime()

        if getHour == 23 and getMinutes == 35:
            itsTimeForDinner()

        if getMinutes == 8 or getMinutes == 20:
            check()

    
        while True:
            notification.notify(
                title = 'water reminder',
                message = '''About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women. ''',
                app_icon = "E:\\Python\\AutomatePython\\reminders\\eatSomeThing\\water.ico",
                timeout = 10
            )
            # har half hour me remind karo
            time.sleep(60*10)   #har 30 min me yeh remind karega pani pine ke liye
            # time.sleep(10)

else:
    print('have some fun babe')
print(getPresentTime.strftime('%H:%M'))
