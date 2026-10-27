
# Day 50: CSV Files in Python

import csv

# 1. Write CSV data using csv.writer()
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Lalitendra", 18, "Diploma CSE"])
    writer.writerow(["Rahul", 19, "Python"])
    writer.writerow(["Priya", 18, "Java"])

print("CSV file created successfully!")

# 2. Read CSV data using csv.reader()
print("\n----- USING csv.reader() -----")

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# 3. Read CSV data using csv.DictReader()
print("\n----- USING csv.DictReader() -----")

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Course:", student["Course"])
        print()

# 4. Write CSV data using csv.DictWriter()
with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Department", "Salary"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "Name": "Arun",
        "Department": "IT",
        "Salary": 25000
    })

    writer.writerow({
        "Name": "Sneha",
        "Department": "HR",
        "Salary": 30000
    })

print("Employee CSV file created successfully!")

# 5. Read employee data
print("\n----- EMPLOYEE RECORDS -----")

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        print(
            employee["Name"],
            employee["Department"],
            employee["Salary"]
        )
