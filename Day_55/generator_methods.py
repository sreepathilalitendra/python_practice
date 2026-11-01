
# Day 55: Generator Methods

# 1. Using next()

def simple_generator():
    yield 100
    yield 200
    yield 300


numbers = simple_generator()

print("Next values:")
print(next(numbers))
print(next(numbers))


# 2. Using send()

def message_generator():

    message = yield "Generator started"

    yield f"Received: {message}"


messages = message_generator()

print("\nSend method:")

print(next(messages))

print(messages.send("Hello Python"))


# 3. Using close()

def close_generator():

    try:
        yield 1
        yield 2
        yield 3

    finally:
        print("Generator closed")


values = close_generator()

print("\nClose method:")

print(next(values))

values.close()
