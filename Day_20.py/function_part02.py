# Day 20 - Functions Part 2


# 1. Multiple Return Values

def calculate(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction


result = calculate(10, 5)

print(result)


# 2. Keyword Arguments

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student(
    name="Sreepathi",
    age=18,
    course="Diploma CSE"
)


# 3. Positional Arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Sreepathi", 18)


# 4. Default + Regular Parameter

def greet(name, message="Welcome"):
    print(message, name)


greet("Sreepathi")
greet("Sreepathi", "Hello")


# 5. *args - Multiple Arguments

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


result = add_numbers(10, 20, 30, 40)

print(result)


# 6. **kwargs - Multiple Keyword Arguments

def student_info(**details):
    for key, value in details.items():
        print(key, value)


student_info(
    name="Sreepathi",
    age=18,
    course="Diploma CSE"
)


# 7. Function Calling Another Function

def greet():
    print("Hello Bro!")


def start():
    greet()
    print("Let's learn Python!")


start()


# 8. Simple Calculator Function

def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)


calculator(10, 5)