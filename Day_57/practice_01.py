

from contextlib import contextmanager


# Challenge 1: Create a file and write five lines

print("Challenge 1: Writing to a file")

with open("challenge_notes.txt", "w") as file:
    file.write("Python Context Managers\n")
    file.write("Learning the with statement\n")
    file.write("Practising file handling\n")
    file.write("Understanding cleanup\n")
    file.write("Day 57 completed\n")

print("File created successfully!")


# Challenge 2: Read the file using with

print("\nChallenge 2: Reading the file")

with open("challenge_notes.txt", "r") as file:
    content = file.read()

print(content)


# Challenge 3 and 4: Custom context manager using a class

class MyContextManager:

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        return False


print("Challenge 3 and 4: Custom Context Manager")

with MyContextManager():
    print("Inside the context manager")


# Challenge 5: Generator-based context manager

@contextmanager
def my_context():

    print("Starting generator context")

    try:
        yield "Generator context is active"
    finally:
        print("Generator context cleanup")


print("\nChallenge 5: Generator Context Manager")

with my_context() as message:
    print(message)


# Challenge 6: Temporarily change a dictionary value

@contextmanager
def temporary_value(dictionary, key, new_value):

    old_value = dictionary[key]
    dictionary[key] = new_value

    try:
        yield dictionary
    finally:
        dictionary[key] = old_value


print("\nChallenge 6: Temporary Dictionary Value")

settings = {
    "theme": "light",
    "language": "English"
}

print("Before:", settings)

with temporary_value(settings, "theme", "dark"):
    print("Inside:", settings)

print("After:", settings)


# Challenge 7: Handle ValueError and ensure cleanup

@contextmanager
def safe_context():

    print("\nStarting safe context")

    try:
        yield
    except ValueError as error:
        print("Handled error:", error)
    finally:
        print("Cleanup completed")


print("\nChallenge 7: Exception Handling")

with safe_context():
    print("Inside safe context")
    raise ValueError("Invalid value detected")

print("Program continues normally")
