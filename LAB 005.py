import datetime
import calendar

price = 123
bonus = 23
bonus_granted = True
price -= bonus if bonus_granted == True else "?"
print(price)

rating = 4

check = "very good" if rating==5 else "good" if rating==4 else "weak"
print(check)

days = list(calendar.day_abbr)
today_weekday = datetime.datetime.now().weekday()
day = (days[today_weekday])
todo = "Programowanie" if day=='Thu' else "?"
print(todo + " Bo dziś jest {}".format(day))

import datetime as dt

today_weekday = dt.date.today().strftime("%A")

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")

print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")