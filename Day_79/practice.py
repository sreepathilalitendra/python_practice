
import os
from dotenv import load_dotenv


# Challenge 1: Read Windows username

windows_username = os.getenv("USERNAME", "Unknown")

print("Windows Username:", windows_username)


# Challenge 2: Set student name

os.environ["STUDENT_NAME"] = "Lalitendra"

print("\nStudent Name:", os.getenv("STUDENT_NAME"))


# Challenge 3: Create student environment variables

os.environ["COURSE"] = "Diploma CSE"
os.environ["COLLEGE"] = "St. Mary's Group of Institutions"


# Challenge 4: Display student details

print("\nStudent Details")

print("Name:", os.getenv("STUDENT_NAME"))
print("Course:", os.getenv("COURSE"))
print("College:", os.getenv("COLLEGE"))


# Challenge 5: Check whether API_KEY exists

api_key = os.getenv("API_KEY")

if api_key:
    print("\nAPI_KEY is configured")
else:
    print("\nAPI_KEY is not configured")


# Challenge 6: Handle missing DATABASE_NAME

database_name = os.getenv("DATABASE_NAME")

if database_name is None:
    print("\nDATABASE_NAME is missing")
else:
    print("\nDatabase Name:", database_name)


# Challenge 7: Create .env file with application settings

env_content = """APP_NAME=CodeMonolith
APP_ENV=Development
DEBUG=True
"""

with open(".env", "w", encoding="utf-8") as file:
    file.write(env_content)

print("\n.env file created successfully")


# Challenge 8: Load .env variables

load_dotenv(override=True)

app_name = os.getenv("APP_NAME")
app_env = os.getenv("APP_ENV")
debug = os.getenv("DEBUG")

print("\nLoaded Environment Variables")
print("Application:", app_name)
print("Environment:", app_env)
print("Debug:", debug)


# Challenge 9: Create application configuration dictionary

app_config = {
    "app_name": os.getenv("APP_NAME", "Unknown"),
    "environment": os.getenv("APP_ENV", "Development"),
    "debug": os.getenv("DEBUG", "False").lower() == "true"
}

print("\nApplication Configuration")

for key, value in app_config.items():
    print(key, ":", value)


# Challenge 10: Mini Student Application Configuration Manager

def student_configuration():

    load_dotenv(override=True)

    student = {
        "name": os.getenv("STUDENT_NAME", "Not Provided"),
        "course": os.getenv("COURSE", "Not Provided"),
        "college": os.getenv("COLLEGE", "Not Provided"),
        "app_name": os.getenv("APP_NAME", "CodeMonolith")
    }

    print("\nStudent Application Configuration")

    for key, value in student.items():
        print(key.replace("_", " ").title(), ":", value)

    print("\nConfiguration Loaded Successfully")


student_configuration()
