# Challenge 1: Power function

def make_power(exponent):
    def power(number):
        return number ** exponent

    return power


square = make_power(2)
cube = make_power(3)

print(square(4))
print(cube(4))


# Challenge 2: Greeting closure

def make_greeting(greeting):
    def greet(name):
        print(f"{greeting}, {name}!")

    return greet


say_hello = make_greeting("Hello")
say_welcome = make_greeting("Welcome")

say_hello("Lalitendra")
say_welcome("Student")


# Challenge 3: Bank balance

def create_balance(initial_balance):
    balance = initial_balance

    def add_money():
        nonlocal balance
        balance += 100
        return balance

    return add_money


balance = create_balance(500)

print(balance())
print(balance())
print(balance())


# Challenge 4: Tax calculator

def make_tax_calculator(tax_percent):
    def calculate(price):
        tax = price * tax_percent / 100
        return price + tax

    return calculate


gst_calculator = make_tax_calculator(18)

print(gst_calculator(1000))
print(gst_calculator(500))


# Challenge 5: Independent counters

def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter_one = create_counter()
counter_two = create_counter()

print(counter_one())  # 1
print(counter_one())  # 2
print(counter_one())  # 3

print(counter_two())  # 1
