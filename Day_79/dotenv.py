import os
from dotenv import load_dotenv


# Load variables from .env

load_dotenv()


# Read variables

student_name = os.getenv("STUDENT_NAME")
college = os.getenv("COLLEGE_NAME")
course = os.getenv("COURSE")
skill = os.getenv("SKILL")


# Display configuration

print("Student Details")

print("Name:", student_name)
print("College:", college)
print("Course:", course)
print("Skill:", skill)


# Read application settings

app_name = os.getenv("APP_NAME")
app_env = os.getenv("APP_ENV")

debug = os.getenv("DEBUG", "False").lower() == "true"

print("\nApplication Details")
print("Application:", app_name)
print("Environment:", app_env)
print("Debug Mode:", debug)
