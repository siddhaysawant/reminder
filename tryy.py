import datetime
getPresentTime = datetime.datetime.now()
getHour = int(getPresentTime.strftime('%H'))
if getHour == 9:
    print('yes')