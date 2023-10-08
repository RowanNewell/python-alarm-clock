import schedule
import time
from plyer import notification


set_alarm = input("What time do you want the alarm to go off? ")
alarm_text = input("What do you want to call this alarm? ")

def alarm_alert():
    #set off alarm
    notification.notify(
        title = alarm_text,
        timeout= 10
    )
alarm_alert()
schedule.every().day.at(set_alarm).do(alarm_alert)

while True:
    schedule.run_pending()
    time.sleep(1)
