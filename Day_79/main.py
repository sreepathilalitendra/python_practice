
import os


# Example 1: Import os module

print("Environment Variables in Python")


# Example 2: Read an environment variable

username = os.getenv("USERNAME")

print("\nWindows Username:", username)


# Example 3: Read a custom variable

college = os.getenv("COLLEGE_NAME", "Not Provided")

print("College:", college)


# Example 4: Set an environment variable

os.environ["STUDENT_NAME"] = "Lalitendra"

student_name = os.getenv("STUDENT_NAME")

print("\nStudent Name:", student_name)


# Example 5: Set multiple variables

os.environ["COURSE"] = "Diploma CSE"
os.environ["SKILL"] = "Python"

print("Course:", os.getenv("COURSE"))
print("Skill:", os.getenv("SKILL"))


# Example 6: Check whether a variable exists

if os.getenv("STUDENT_NAME"):
    print("\nStudent Name Variable Exists")
else:
    print("\nStudent Name Variable Missing")


# Example 7: Handle missing variables

api_key = os.getenv("API_KEY")

if api_key:
    print("API Key is available")
else:
    print("API Key is not configured")


# Example 8: Read environment variables safely

database_name = os.getenv("DATABASE_NAME")

if database_name is None:
    print("\nDatabase Name Not Configured")
else:
    print("\nDatabase:", database_name)


# Example 9: Display selected environment settings

settings = {
    "Student": os.getenv("STUDENT_NAME"),
    "Course": os.getenv("COURSE"),
    "Skill": os.getenv("SKILL")
}

print("\nApplication Settings")

for key, value in settings.items():
    print(key, ":", value)


# Example 10: Create an application configuration

app_config = {
    "app_name": os.getenv("APP_NAME", "CodeMonolith"),
    "environment": os.getenv("APP_ENV", "Development"),
    "debug": os.getenv("DEBUG", "False").lower() == "true"
}

print("\nApplication Configuration")

for key, value in app_config.items():
    print(key, ":", value)
