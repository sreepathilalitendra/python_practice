
from datetime import (
    date,
    time,
    datetime,
    timedelta,
    timezone
)

from zoneinfo import ZoneInfo
import calendar


# Example 1: date()

print("EXAMPLE 1: DATE")

today = date.today()

print("Today's Date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Example 2: time()

print("\nEXAMPLE 2: TIME")

current_time = datetime.now().time()

print("Current Time:", current_time)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)

custom_time = time(10, 30, 45)

print("Custom Time:", custom_time)


# Example 3: datetime()

print("\nEXAMPLE 3: DATETIME")

current_datetime = datetime.now()

print("Current Date and Time:", current_datetime)
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)


# Example 4: timedelta()

print("\nEXAMPLE 4: TIMEDELTA")

today = date.today()

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

after_30_days = today + timedelta(days=30)

print("Today:", today)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
print("After 30 Days:", after_30_days)


# Example 5: strftime()

print("\nEXAMPLE 5: STRFTIME")

now = datetime.now()

formatted_date = now.strftime("%d-%m-%Y")
formatted_time = now.strftime("%H:%M:%S")
formatted_day = now.strftime("%A")

print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)
print("Day Name:", formatted_day)


# Example 6: strptime()

print("\nEXAMPLE 6: STRPTIME")

date_string = "16-11-2026"

converted_date = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print("Original String:", date_string)
print("Converted Date:", converted_date)
print("Year:", converted_date.year)


# Example 7: timezone()

print("\nEXAMPLE 7: UTC TIMEZONE")

utc_time = datetime.now(timezone.utc)

print("UTC Date and Time:", utc_time)

india_timezone = timezone(timedelta(hours=5, minutes=30))

india_time = utc_time.astimezone(india_timezone)

print("India Date and Time:", india_time)


# Example 8: ZoneInfo()

print("\nEXAMPLE 8: ZONEINFO")

india_time = datetime.now(
    ZoneInfo("Asia/Kolkata")
)

london_time = datetime.now(
    ZoneInfo("Europe/London")
)

new_york_time = datetime.now(
    ZoneInfo("America/New_York")
)

print("India:", india_time)
print("London:", london_time)
print("New York:", new_york_time)


# Example 9: calendar()

print("\nEXAMPLE 9: CALENDAR")

year = 2026
month = 11

print(calendar.month(year, month))

print("Is Leap Year:", calendar.isleap(year))


# Mini Project: Age Calculator

print("\nMINI PROJECT: AGE CALCULATOR")

birth_date_string = "15-08-2008"

birth_date = datetime.strptime(
    birth_date_string,
    "%d-%m-%Y"
).date()

today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (
    birth_date.month,
    birth_date.day
):
    age -= 1

print("Birth Date:", birth_date)
print("Current Date:", today)
print("Age:", age, "years")


print("\nDAY 70 MAIN LESSON COMPLETED!")
