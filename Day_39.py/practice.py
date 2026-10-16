# CHALLENGE 1: Find the largest number using *args

def find_largest(*args):
    if not args:
        return None

    return max(args)


print(find_largest(10, 50, 30, 80, 20))


# CHALLENGE 2: Calculate the average using *args

def calculate_average(*args):
    if not args:
        return None

    return sum(args) / len(args)


print(calculate_average(10, 20, 30, 40))


# CHALLENGE 3: Display a user profile using **kwargs

def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


user_profile(
    name="Ravi",
    age=18,
    skill="Python"
)


# CHALLENGE 4: Combine a name and multiple marks

def display_marks(name, *marks):
    print("Student:", name)
    print("Marks:", marks)
    print("Total:", sum(marks))


display_marks("Anu", 80, 75, 90)


# CHALLENGE 5: Create a product using keyword arguments

def product_details(name, **details):
    print("Product:", name)

    for key, value in details.items():
        print(f"{key}: {value}")


product_details(
    "Laptop",
    brand="Dell",
    ram="16GB",
    price=50000
)


# CHALLENGE 6: Use keyword-only arguments

def login(*, username, password):
    print("Username:", username)
    print("Password received")


login(username="student01", password="example123")


# CHALLENGE 7: Unpack a list into a function

def calculate_sum(a, b, c):
    return a + b + c


values = [10, 20, 30]

print("Sum:", calculate_sum(*values))


# CHALLENGE 8: Unpack a dictionary into a function

def display_student(name, course, city):
    print("Name:", name)
    print("Course:", course)
    print("City:", city)


student_data = {
    "name": "Ravi",
    "course": "CSE",
    "city": "Hyderabad"
}

display_student(**student_data)