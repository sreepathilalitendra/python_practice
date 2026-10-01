# Day 24 - Datetime Module

import datetime


# Current Date
today = datetime.date.today()
print(today)


# Current Date and Time
now = datetime.datetime.now()
print(now)


# Individual Date Values
today = datetime.date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Creating a Specific Date
date = datetime.date(2026, 10, 1)
print(date)


# Formatting Date
today = datetime.date.today()

print(today.strftime("%d-%m-%Y"))


# Creating a Specific Time
time = datetime.time(10, 30, 45)
print(time)


# Current Time
now = datetime.datetime.now()

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)