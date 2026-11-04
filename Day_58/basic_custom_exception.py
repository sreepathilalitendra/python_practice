
# Day 58: Basic Custom Exception

class InvalidAgeError(Exception):
    pass


age = 15

try:

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Access granted!")

except InvalidAgeError as error:
    print("Custom Error:", error)
