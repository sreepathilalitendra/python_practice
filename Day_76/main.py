
import json

# Example 1: API information

api_name = "Student Management API"
api_version = "1.0"

print("API Name:", api_name)
print("API Version:", api_version)


# Example 2: HTTP methods

http_methods = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE"
]

print("\nHTTP Methods:")

for method in http_methods:
    print(method)


# Example 3: HTTP status codes

status_codes = {
    200: "OK",
    201: "Created",
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found",
    500: "Internal Server Error"
}

print("\nHTTP Status Codes:")

for code, message in status_codes.items():
    print(code, "-", message)


# Example 4: API endpoint

base_url = "https://example.com/api"

endpoint = "/students"

full_url = base_url + endpoint

print("\nAPI Endpoint:", full_url)


# Example 5: Client request simulation

request = {
    "method": "GET",
    "endpoint": "/students",
    "headers": {
        "Accept": "application/json"
    }
}

print("\nRequest:")

print(json.dumps(request, indent=4))


# Example 6: Server response simulation

response = {
    "status_code": 200,
    "message": "Students retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "Lalitendra",
            "course": "Diploma CSE"
        },
        {
            "id": 2,
            "name": "Rahul",
            "course": "Diploma CSE"
        }
    ]
}

print("\nServer Response:")

print(json.dumps(response, indent=4))


# Example 7: Convert dictionary into JSON

student = {
    "name": "Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}

student_json = json.dumps(student, indent=4)

print("\nJSON Data:")
print(student_json)


# Example 8: Convert JSON into dictionary

student_data = json.loads(student_json)

print("\nStudent Name:", student_data["name"])
print("Student Course:", student_data["course"])


# Example 9: Simulate POST request

new_student = {
    "id": 3,
    "name": "Arjun",
    "course": "Diploma CSE"
}

print("\nPOST Request:")
print(json.dumps(new_student, indent=4))

print("Status Code: 201")
print("Student created successfully")


# Example 10: Simulate DELETE request

delete_student_id = 3

print("\nDELETE Request:")
print("Deleting student ID:", delete_student_id)

print("Status Code: 204")
print("Student deleted successfully")
