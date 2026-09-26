# Challenge 1
# Create a function called greet()
# and print "Hello Python".

def greet():
    print("Hello Python")

greet()


# Challenge 2
# Create a function that accepts a name
# and prints the name.

def print_name(name):
    print(name)

print_name("Sreepathi Lalitendra")


# Challenge 3
# Create a function with two numbers
# and print their sum.

def add(a, b):
    print(a + b)

add(10, 20)


# Challenge 4
# Create a function that accepts a number
# and checks whether it is even or odd.

def check_number(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_number(10)
check_number(7)


# Challenge 5
# Create a function that accepts a number
# and returns its square.

def square(number):
    return number * number

result = square(5)

print(result)


# Challenge 6 
# Create a function that accepts name, age, and course
# and prints all three.

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student("Sreepathi Lalitendra", 18, "Diploma CSE")


# Challenge 7 
# Create a function that prints numbers
# from 1 to 10 using a for loop.

def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()