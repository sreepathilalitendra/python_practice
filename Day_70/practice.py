
from datetime import date, time, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import calendar


# Challenge 1: Today's Date

print("CHALLENGE 1: TODAY'S DATE")

today = date.today()

print("Today's Date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Challenge 2: Current Time

print("\nCHALLENGE 2: CURRENT TIME")

current_time = datetime.now().time()

print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)


# Challenge 3: Date After 100 Days

print("\nCHALLENGE 3: AFTER 100 DAYS")

today = date.today()

future_date = today + timedelta(days=100)

print("Today:", today)
print("After 100 Days:", future_date)


# Challenge 4: Date Before 50 Days

print("\nCHALLENGE 4: BEFORE 50 DAYS")

today = date.today()

past_date = today - timedelta(days=50)

print("Today:", today)
print("Before 50 Days:", past_date)


# Challenge 5: Convert String into Datetime

print("\nCHALLENGE 5: STRPTIME")

date_string = "25-12-2026"

converted_date = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print("Original String:", date_string)
print("Converted Date:", converted_date)


# Challenge 6: Format Today's Date

print("\nCHALLENGE 6: STRFTIME")

today = datetime.now()

formatted_date = today.strftime("%d/%m/%Y")

print("Formatted Date:", formatted_date)


# Challenge 7: UTC and India Time

print("\nCHALLENGE 7: UTC AND INDIA TIME")

utc_time = datetime.now(timezone.utc)

india_time = utc_time.astimezone(
    ZoneInfo("Asia/Kolkata")
)

print("UTC Time:", utc_time)
print("India Time:", india_time)


# Challenge 8: Different Country Time Zones

print("\nCHALLENGE 8: WORLD TIME")

india_time = datetime.now(
    ZoneInfo("Asia/Kolkata")
)

london_time = datetime.now(
    ZoneInfo("Europe/London")
)

new_york_time = datetime.now(
    ZoneInfo("America/New_York")
)

print("India:", india_time.strftime("%d-%m-%Y %H:%M:%S"))
print("London:", london_time.strftime("%d-%m-%Y %H:%M:%S"))
print("New York:", new_york_time.strftime("%d-%m-%Y %H:%M:%S"))


# Challenge 9: December 2026 Calendar

print("\nCHALLENGE 9: DECEMBER 2026 CALENDAR")

print(calendar.month(2026, 12))


# Challenge 10: Birthday Countdown Calculator

print("\nCHALLENGE 10: BIRTHDAY COUNTDOWN")

today = date.today()

birth_date = date(2008, 8, 15)

next_birthday = date(
    today.year,
    birth_date.month,
    birth_date.day
)

if next_birthday < today:
    next_birthday = date(
        today.year + 1,
        birth_date.month,
        birth_date.day
    )

days_remaining = (next_birthday - today).days

print("Today:", today)
print("Next Birthday:", next_birthday)
print("Days Remaining:", days_remaining)


print("\nDAY 70 CHALLENGES COMPLETED!")
