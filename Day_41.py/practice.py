# Challenge 1: Local scope

def student_info():
    student_name = "Lalitendra"
    print(student_name)


student_info()


# Challenge 2: Global scope

points = 10


def increase_points():
    global points
    points += 5


increase_points()
print("Points:", points)


# Challenge 3: Local vs global

color = "blue"


def show_colors():
    color = "red"
    print("Local color:", color)


show_colors()
print("Global color:", color)


# Challenge 4: Nonlocal scope

def outer_function():
    number = 10

    def inner_function():
        nonlocal number
        number += 5

    inner_function()
    print("Updated number:", number)


outer_function()


# Challenge 5: LEGB

x = "Global"


def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print("Inner:", x)

    inner()
    print("Outer:", x)


outer()
print("Global:", x)
