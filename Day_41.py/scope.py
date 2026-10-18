
# Day 41: Scope in Python

# 1. Local variable

def greet():
    message = "Hello, Python!"
    print(message)


greet()


# 2. Global variable

name = "Lalitendra"


def display_name():
    print(name)


display_name()
print(name)


# 3. Local variable with the same name as a global variable

score = 100


def show_score():
    score = 50
    print("Local score:", score)


show_score()
print("Global score:", score)


# 4. Using the global keyword

count = 0


def increase_count():
    global count
    count += 1


increase_count()
increase_count()

print("Count:", count)


# 5. Enclosing scope and nonlocal

def outer_function():
    message = "Original message"

    def inner_function():
        nonlocal message
        message = "Updated message"

    inner_function()
    print(message)


outer_function()


# 6. LEGB example

language = "Python"


def outer():
    language = "Java"

    def inner():
        language = "C++"
        print("Inner:", language)

    inner()
    print("Outer:", language)


outer()
print("Global:", language)
