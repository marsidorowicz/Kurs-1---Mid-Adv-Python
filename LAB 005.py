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