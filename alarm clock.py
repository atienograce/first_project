import datetime

alarmHour = int(input("What hour do you want to wake up? "))
alarmMinute = int(input("What minute do you want to wake up? "))
amPm = str(input("am or pm? "))

if (amPm == 'pm'):
    alarmHour += + 12

while True:
    if (alarmHour == datetime.datetime.now().hour and
    alarmMinute == datetime.datetime.now().minute):
     print("Wake up lazy bones")
     break

print("yo!")

