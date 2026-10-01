# Challenge 1 - Current Date
import datetime

today = datetime.date.today()

print(today)


# Challenge 2 - Current Date & Time
import datetime

now = datetime.datetime.now()

print(now)


# Challenge 3 - Date Details
import datetime

today = datetime.date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Challenge 4 - Specific Date
import datetime

date = datetime.date(2026, 12, 25)

print(date)


# Challenge 5 - Date Formatting
import datetime

today = datetime.date.today()

print(today.strftime("%d-%m-%Y"))


# Challenge 6 - Specific Time
import datetime

time = datetime.time(10, 30, 45)

print(time)


# Challenge 7 - Current Time Details
import datetime

now = datetime.datetime.now()

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


# Challenge 8 - Day/Month/Year Format
import datetime

today = datetime.date.today()

print(today.strftime("%Y/%m/%d"))


# Challenge 9 - Month Name
import datetime

today = datetime.date.today()

print(today.strftime("%B"))


# Challenge 10 - Date & Time Program
import datetime

now = datetime.datetime.now()

print("Date:", now.strftime("%d-%m-%Y"))
print("Time:", now.strftime("%H:%M:%S"))