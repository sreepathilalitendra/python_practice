
import json


# Challenge 1: Display five HTTP methods

http_methods = {
    "GET": "Retrieve data",
    "POST": "Create new data",
    "PUT": "Replace existing data",
    "PATCH": "Update part of existing data",
    "DELETE": "Delete data"
}

for method, purpose in http_methods.items():
    print(method, ":", purpose)


# Challenge 2: Display HTTP status codes

status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found",
    500: "Internal Server Error"
}

for code, meaning in status_codes.items():
    print(code, ":", meaning)


# Challenge 3: Create a student API endpoint

endpoint = "/api/students"

print("Student API Endpoint:", endpoint)


# Challenge 4: Create a JSON object

student = {
    "id": 101,
    "name": "Lalitendra",
    "course": "Diploma CSE",
    "college": "St. Mary's Group of Institutions"
}

print(json.dumps(student, indent=4))


# Challenge 5: Convert Python dictionary into JSON

student_json = json.dumps(student, indent=4)

print(student_json)


# Challenge 6: Convert JSON into Python dictionary

student_data = json.loads(student_json)

print("Student Name:", student_data["name"])
print("Course:", student_data["course"])


# Challenge 7: Simulate a GET request

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Arjun"},
    {"id": 3, "name": "Priya"}
]

print("GET Request")
print("Status Code: 200")
print("Response:", json.dumps(students, indent=4))


# Challenge 8: Simulate a POST request

new_student = {
    "id": 4,
    "name": "Kiran"
}

students.append(new_student)

print("POST Request")
print("Status Code: 201")
print("New Student Added:", new_student)


# Challenge 9: Simulate PUT and PATCH requests

student_record = {
    "id": 1,
    "name": "Rahul",
    "course": "CSE"
}

# PUT: Replace the complete record
student_record = {
    "id": 1,
    "name": "Rahul Kumar",
    "course": "ECE"
}

print("After PUT:", student_record)

# PATCH: Update only one field
student_record["course"] = "CSE"

print("After PATCH:", student_record)


# Challenge 10: Mini Student API Simulator

student_database = {
    101: {
        "name": "Lalitendra",
        "course": "Diploma CSE"
    }
}


def get_student(student_id):
    if student_id in student_database:
        return {
            "status": 200,
            "data": student_database[student_id]
        }

    return {
        "status": 404,
        "message": "Student not found"
    }


def add_student(student_id, name, course):
    if student_id in student_database:
        return {
            "status": 400,
            "message": "Student already exists"
        }

    student_database[student_id] = {
        "name": name,
        "course": course
    }

    return {
        "status": 201,
        "message": "Student created successfully"
    }


print("\nGET Response:")
print(json.dumps(get_student(101), indent=4))

print("\nPOST Response:")
print(json.dumps(
    add_student(102, "Arjun", "Diploma CSE"),
    indent=4
))

print("\nUpdated Student Database:")
print(json.dumps(student_database, indent=4))
