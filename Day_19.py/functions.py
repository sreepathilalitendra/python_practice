# Day 19 - Functions


# 1. Creating a Function

def greet():
    print("Hello Bro!")

greet()


# 2. Function with a Parameter

def greet(name):
    print("Hello", name)

greet("Sreepathi Lalitendra")


# 3. Function with Multiple Parameters

def add(a, b):
    print(a + b)

add(10, 20)


# 4. Returning a Value - return

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# 5. Function with Different Data

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student("Sreepathi Lalitendra", 18, "Diploma CSE")


# 6. Default Parameter

def greet(name="Bro"):
    print("Hello", name)

greet()


# 7. Function with a Condition

def check_number(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_number(10)
check_number(7)


# 8. Function with a Loop

def print_number():
    for i in range(1, 6):
        print(i)

print_number()