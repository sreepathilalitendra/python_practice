# LESSON 1: Using *args

def display_numbers(*args):
    print("Numbers:", args)


display_numbers(10, 20, 30)
display_numbers(1, 2, 3, 4, 5)


# LESSON 2: Calculate a total using *args

def calculate_total(*args):
    return sum(args)


print(calculate_total(10, 20, 30))
print(calculate_total(5, 15, 25, 35))


# LESSON 3: Using **kwargs

def display_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


display_details(name="Ravi", age=18, course="CSE")


# LESSON 4: Combine regular arguments and *args

def calculate_bill(customer, *prices):
    print("Customer:", customer)
    print("Total bill:", sum(prices))


calculate_bill("Ravi", 100, 200, 50)


# LESSON 5: Combine regular arguments and **kwargs

def employee_details(employee_id, **details):
    print("Employee ID:", employee_id)

    for key, value in details.items():
        print(key, ":", value)


employee_details(
    101,
    name="Anu",
    department="IT",
    experience=2
)


# LESSON 6: Combine *args and **kwargs

def show_information(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


show_information(10, 20, 30, name="Ravi", course="Python")


# LESSON 7: Keyword-only arguments

def create_profile(name, *, city, course):
    print("Name:", name)
    print("City:", city)
    print("Course:", course)


create_profile(
    "Lalitendra",
    city="Hyderabad",
    course="Python"
)


# LESSON 8: Unpacking a list using *

def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]

print(multiply(*numbers))


# LESSON 9: Unpacking a dictionary using **

def student(name, course):
    print("Name:", name)
    print("Course:", course)


details = {
    "name": "Ravi",
    "course": "Python"
}

student(**details)


# LESSON 10: Default arguments

def greet(name, message="Welcome"):
    print(message, name)


greet("Ravi")
greet("Anu", "Good morning")