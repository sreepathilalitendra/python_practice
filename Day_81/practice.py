
import sqlite3


# Challenge 1: Create employee database

connection = sqlite3.connect("employee.db")

cursor = connection.cursor()

print("Employee Database Created Successfully")


# Challenge 2: Create employees table

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

connection.commit()

print("Employees Table Created")


# Challenge 3: Insert five employee records

employees = [
    ("Rahul", "IT", 30000),
    ("Arjun", "HR", 25000),
    ("Priya", "Finance", 35000),
    ("Kiran", "IT", 40000),
    ("Sneha", "Marketing", 28000)
]

cursor.executemany("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", employees)

connection.commit()

print("Five Employees Inserted Successfully")


# Challenge 4: Display all employees

def display_employees():

    cursor.execute("SELECT * FROM employees")

    records = cursor.fetchall()

    print("\nAll Employee Records")

    if not records:
        print("No Employees Found")
        return

    for employee in records:
        print(employee)


display_employees()


# Challenge 5: Search employee using ID

def search_employee(employee_id):

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if employee:
        print("\nEmployee Found")
        print(employee)
    else:
        print("\nEmployee Not Found")


search_employee(1)


# Challenge 6: Update employee salary

def update_salary(employee_id, new_salary):

    cursor.execute("""
    UPDATE employees
    SET salary = ?
    WHERE id = ?
    """, (new_salary, employee_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("\nSalary Updated Successfully")
    else:
        print("\nEmployee Not Found")


update_salary(1, 45000)


# Challenge 7: Delete employee using ID

def delete_employee(employee_id):

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("\nEmployee Deleted Successfully")
    else:
        print("\nEmployee Not Found")


delete_employee(5)


# Challenge 8: Display employees with salary > 25000

cursor.execute("""
SELECT * FROM employees
WHERE salary > ?
""", (25000,))

high_salary_employees = cursor.fetchall()

print("\nEmployees with Salary Greater Than 25000")

for employee in high_salary_employees:
    print(employee)


# Challenge 9: Sort employees by salary

cursor.execute("""
SELECT * FROM employees
ORDER BY salary DESC
""")

sorted_employees = cursor.fetchall()

print("\nEmployees Sorted by Salary")

for employee in sorted_employees:
    print(employee)


# Challenge 10: Mini Employee Management System

def add_employee(name, department, salary):

    cursor.execute("""
    INSERT INTO employees (name, department, salary)
    VALUES (?, ?, ?)
    """, (name, department, salary))

    connection.commit()

    print("Employee Added Successfully")


def view_employees():

    cursor.execute("SELECT * FROM employees")

    records = cursor.fetchall()

    print("\nEmployee List")

    for employee in records:
        print(employee)


def find_employee(employee_id):

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    result = cursor.fetchone()

    if result:
        print("\nEmployee Details:", result)
    else:
        print("\nEmployee Not Found")


def change_salary(employee_id, salary):

    cursor.execute("""
    UPDATE employees
    SET salary = ?
    WHERE id = ?
    """, (salary, employee_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Employee Salary Updated")
    else:
        print("Employee Not Found")


def remove_employee(employee_id):

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Employee Removed")
    else:
        print("Employee Not Found")


# Demonstrate all operations

print("\nEmployee Management System")

add_employee("Lalitendra", "IT", 50000)

view_employees()

find_employee(6)

change_salary(6, 55000)

remove_employee(6)

view_employees()


# Close database connection

connection.close()

print("\nDatabase Connection Closed")
