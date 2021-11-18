''' yeh program me apan reminder ko sey karne wale hai jo ki apne ko remind karega task ko complete karne ke liye'''

import datetime
import time
from plyer import notification
import os
os.system('cls')

'''
NOTE--> idr mene galti kiya tha mene presentTime sidha yaha peh likha and uske karan mera getPresentTime update hi nahi hopaya and the update na hone ke karan time sif constant show horaha tha so mene getPresentTime ko sidha while loop me execute kiya and yaha wala the getPResentTime usko mene comment out kiya 

getPresentTime = datetime.datetime.now()
getHour = int(getPresentTime.strftime('%H'))
getMinutes = int(getPresentTime.strftime('%M'))
'''

'''here all functionss will be defined '''
def greetSiddhay(Name):
    notification.notify(
        title = f'Good Morning {Name}',
        message = "I hope this morning you will be more productive than yesterday",
        app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\4536362.ico",
        timeout = 10 #10 seconds tak notification rahega
    )

def eatLunchSiddhay():
    notification.notify(
        title = f'Time For Lunch ',
        message = "According to experts, lunch provides nourishment to the body and brain and reduces stress and eating lunch provides a break from the activities of the day and gives energy for the rest of the afternoon. ",
        app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\4536362.ico",
        timeout = 10 #10 seconds tak notification rahega
    )

def haveAfternoonBreakfast():
    notification.notify(
        title = f'Time For Afternoon breakfast ',
        message = "Breakfast kick-starts your metabolism, helping you burn calories throughout the day. ... Many studies have linked eating breakfast to good health, including better memory and concentration, lower levels of “bad” LDL cholesterol, and lower chances of getting diabetes, heart disease, and being overweight.x ",
        app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\4536362.ico",
        timeout = 10 #10 seconds tak notification rahega
    )

def eatBreakfast():
    notification.notify(
        title = f'Time For breakfast ',
        message = "Breakfast kick-starts your metabolism, helping you burn calories throughout the day. ... Many studies have linked eating breakfast to good health, including better memory and concentration, lower levels of “bad” LDL cholesterol, and lower chances of getting diabetes, heart disease, and being overweight.x ",
        app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\4536362.ico",
        timeout = 10 #10 seconds tak notification rahega
    )

def waterReminder():
    '''notification.notify--> agar message bhot bada hogaya a toh fir woh error throw karega so message ko short rakhne ka '''

    notification.notify(    
        title = "Please drink water",
        message = "Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
        # app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\water.ico",
        app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\4536362.ico",
        timeout = 10
    )
    '''this will remind to drink water every 10 min'''
    
def eatDinner():
    notification.notify(
        title = f'Time For Dinner ',
        message = "Eating dinner early gives your body more time to stabilize blood sugar levels, which plays a role in making you feel less fatigued and irritable. Moreover, eating early gives you more energy to perform activities before bed.",
        app_icon = "C:\\programming\\python\\AutomatePython\\reminders\\eatSomeThing\\4536362.ico",
        timeout = 10 #10 seconds tak notification rahega
    )


'''from here main function will be executed'''
if __name__ == '__main__':
    while True:
        # this will update the clock because of the while loop yeh fir while loop ke base peh datetime module khud ke time ko update karta rahega 
        '''
        print(datetime.datetime.now().strftime('%H%M'),end = '\r')  -->this will print the whole clock means iske andr pura hours minute and time rahega 
        '''

        ''' mene yeh while loop ke andr likha hia kyuki yeh fir datetime module khud ko update karta rahega '''
        getPresentTime = datetime.datetime.now()
        getHour = str(getPresentTime.strftime('%H'))
        getMinutes = str(getPresentTime.strftime('%M'))

        # print(getHour,getMinutes) -->this will return the recent hour and recent minute and yeh mene print kiya hai check karne ke liye ki yeh properly update horaha hai ya nahi dekhne ko
        print(datetime.datetime.now().strftime('%H:%M:%S'))
        time.sleep (1)

        ''' for water '''
        # waterReminder() #sidha reminder hai function agar yeh kam karega toh fir yeh sidha sleep ka use karta hai jiske karan time sleep hoga and fir woh sidha given time peh active hoga

        ''' for greet '''
        if getHour == '10' and getMinutes == '00':
            greetSiddhay()
            break
        
        ''' for breakfast '''
        if getHour == '10' and getMinutes == '30':
            eatBreakfast()

        ''' for lunch '''  
        if getHour == '15' and getMinutes == '28':
            eatLunchSiddhay()
            print('lunch program executed succesfully')
            break
        
        ''' for afternoon break '''
        if getHour == '18' and getMinutes == '30':
            haveAfternoonBreakfast()
            print('Afternoon break program executed succesfully')
            break
        
        if getHour == '21' and getMinutes == '30':
            eatDinner()
            print('Dinner program executed succesfully')
            break
        

        
              
        # '''and jaise hi condition match hoga tabh fir yeh message print hoga '''
        

        