
import requests
import json


# Example 1: Get API response

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

response.raise_for_status()

data = response.json()

print("API Response Received")
print("Total Users:", len(data))


# Example 2: Access JSON object

first_user = data[0]

print("\nFirst User")
print("ID:", first_user["id"])
print("Name:", first_user["name"])
print("Email:", first_user["email"])


# Example 3: Access nested JSON data

address = first_user["address"]

print("\nAddress Details")
print("Street:", address["street"])
print("City:", address["city"])
print("Zipcode:", address["zipcode"])


# Example 4: Access deeply nested data

company = first_user["company"]

print("\nCompany Details")
print("Company:", company["name"])
print("Catch Phrase:", company["catchPhrase"])


# Example 5: Use get() to handle missing fields

phone = first_user.get("phone", "Not Available")

print("\nPhone:", phone)


# Example 6: Filter users

print("\nUsers with ID greater than 5")

for user in data:
    if user["id"] > 5:
        print(user["id"], user["name"])


# Example 7: Search for a user

search_name = "Leanne Graham"

found_user = None

for user in data:
    if user["name"].lower() == search_name.lower():
        found_user = user
        break

if found_user:
    print("\nUser Found:", found_user["name"])
else:
    print("\nUser Not Found")


# Example 8: Sort users by name

sorted_users = sorted(
    data,
    key=lambda user: user["name"]
)

print("\nUsers Sorted by Name")

for user in sorted_users:
    print(user["name"])


# Example 9: Save API response into JSON file

with open("users.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("\nAPI data saved successfully")


# Example 10: Read JSON file

with open("users.json", "r", encoding="utf-8") as file:
    saved_data = json.load(file)

print("\nReading Saved JSON Data")

for user in saved_data:
    print(user["id"], user["name"], user["email"])


# Example 11: Convert Python dictionary into JSON string

student = {
    "name": "Lalitendra",
    "course": "Diploma CSE",
    "skill": "Python"
}

json_string = json.dumps(student, indent=4)

print("\nJSON String")
print(json_string)


# Example 12: Convert JSON string into Python dictionary

python_data = json.loads(json_string)

print("\nPython Dictionary")
print(python_data)

print("Student Name:", python_data["name"])
