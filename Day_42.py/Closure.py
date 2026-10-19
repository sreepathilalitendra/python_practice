
# Day 42: Closures in Python

# 1. Basic closure

def outer_function():
    message = "Hello from the outer function!"

    def inner_function():
        print(message)

    return inner_function


my_function = outer_function()
my_function()


# 2. Closure remembers a name

def greet(name):
    def greeting():
        print(f"Hello, {name}!")

    return greeting


greet_lalitendra = greet("Lalitendra")
greet_lalitendra()

greet_student = greet("Student")
greet_student()


# 3. Closure with a calculation

def multiplier(number):
    def multiply(value):
        return value * number

    return multiply


double = multiplier(2)
triple = multiplier(3)

print("Double:", double(5))
print("Triple:", triple(5))


# 4. Closure with remembered state

def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


my_counter = create_counter()

print(my_counter())
print(my_counter())
print(my_counter())


# 5. Two independent counters

counter_a = create_counter()
counter_b = create_counter()

print("Counter A:", counter_a())
print("Counter A:", counter_a())

print("Counter B:", counter_b())


# 6. Closure with a discount

def make_discount(discount_percent):
    def calculate(price):
        discount = price * discount_percent / 100
        return price - discount

    return calculate


student_discount = make_discount(10)

print("Final price:", student_discount(1000))
print("Final price:", student_discount(500))
