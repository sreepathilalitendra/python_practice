# Challenge 1
# Create a function that accepts two numbers
# and returns both their sum and difference.

def calculate(a, b):
    addition = a + b
    difference = a - b

    return addition, difference


result = calculate(20, 10)

print(result)


# Challenge 2
# Create a student() function with name, age, and course.
# Call it using keyword arguments.

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student(
    name="Sreepathi",
    age=18,
    course="Diploma CSE"
)


# Challenge 3
# Create a function with two parameters
# and call it using positional arguments.

def add(a, b):
    print("Sum:", a + b)


add(10, 20)


# Challenge 4
# Create a function with a default parameter "Welcome".

def greet(name, message="Welcome"):
    print(message, name)


greet("Sreepathi")


# Challenge 5 🔥
# Create a function using *args
# that adds any number of numbers.

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


result = add_numbers(10, 20, 30, 40)

print(result)


# Challenge 6 🔥
# Create a function using **kwargs
# and print all the keys and values.

def student_info(**details):
    for key, value in details.items():
        print(key, value)


student_info(
    name="Sreepathi",
    age=18,
    course="Diploma CSE"
)


# Challenge 7 🔥
# Create two functions where one function
# calls the other function.

def greet():
    print("Hello Bro!")


def start():
    greet()
    print("Let's learn Python!")


start()


# Challenge 8 
# Create a calculator function that performs
# addition, subtraction, multiplication, and division.

def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)


calculator(10, 5)