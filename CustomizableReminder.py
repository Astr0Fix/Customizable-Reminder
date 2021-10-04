#Libraries to import#
import time
from plyer import notification

#The text for the reminders and the time for the reminders# 
reminder = input("Input Reminder Text Here: ")
when = input("How often would you like a reminder(in seconds): ")
when = int(when)
times = input("How many times would you like the reminder to be sent: ")
times = int(times)

print("Starting Countdown to Reminder...")
#The reminder code#
while times:
    time.sleep(when)
    notification.notify(title = "Reminder",
                    message = reminder,
                    app_icon = None,
                    timeout = 10,
                    toast = False)
    print(reminder)
    print(times, "Remaining Reminders")
    times -= 1
#Finished Reminder Code#
print("Finished Reminding")