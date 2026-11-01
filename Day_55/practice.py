


# Challenge 1: Convert a tuple into an iterator

numbers = (10, 20, 30, 40, 50)

number_iterator = iter(numbers)

print("Challenge 1: Tuple Iterator")

for number in number_iterator:
    print(number)


# Challenge 2: Custom iterator from 1 to 10

class CountNumbers:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


print("\nChallenge 2: Custom Iterator")

counter = CountNumbers(10)

for number in counter:
    print(number)


# Challenge 3: Generator from 1 to 20

def generate_numbers():

    for number in range(1, 21):
        yield number


print("\nChallenge 3: Numbers from 1 to 20")

for number in generate_numbers():
    print(number)


# Challenge 4: Generate odd numbers from 1 to 30

def odd_numbers():

    for number in range(1, 31, 2):
        yield number


print("\nChallenge 4: Odd Numbers")

for number in odd_numbers():
    print(number)


# Challenge 5: Multiplication table generator

def multiplication_table(number):

    for value in range(1, 11):
        yield f"{number} x {value} = {number * value}"


print("\nChallenge 5: Multiplication Table")

for result in multiplication_table(5):
    print(result)


# Challenge 6: Use send() to send a message

def message_generator():

    message = yield "Generator started"

    yield f"Received message: {message}"


print("\nChallenge 6: Send Method")

messages = message_generator()

print(next(messages))
print(messages.send("Hello Python"))


# Challenge 7: Use close() to stop a generator

def simple_generator():

    try:
        yield 100
        yield 200
        yield 300

    finally:
        print("Generator stopped successfully")


print("\nChallenge 7: Close Method")

values = simple_generator()

print(next(values))

values.close()
