import schedule
import datetime

now = datetime.datetime.now()

def job():
    print("I'm working...")

print(now.strftime("%y/%m/%d - %H/%M/%S"))

# schedule.every().day.at("")