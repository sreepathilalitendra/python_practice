
# Challenge 1: Invalid Age

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Access granted!")


print("Challenge 1: Invalid Age")

try:
    check_age(20)
    check_age(15)
except InvalidAgeError as error:
    print("Error:", error)


# Challenge 2: Invalid Marks

class InvalidMarksError(Exception):
    pass


def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)


print("\nChallenge 2: Invalid Marks")

try:
    check_marks(85)
    check_marks(120)
except InvalidMarksError as error:
    print("Error:", error)


# Challenge 3: Insufficient Balance

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    remaining_balance = balance - amount
    print("Remaining balance:", remaining_balance)


print("\nChallenge 3: Insufficient Balance")

try:
    withdraw(5000, 2000)
    withdraw(3000, 4000)
except InsufficientBalanceError as error:
    print("Error:", error)


# Challenge 4: Student Not Found

class StudentNotFoundError(Exception):
    pass


students = {
    101: "Lalitendra",
    102: "Arun",
    103: "Kiran"
}


def find_student(student_id):
    if student_id not in students:
        raise StudentNotFoundError("Student ID not found.")

    print("Student name:", students[student_id])


print("\nChallenge 4: Student Not Found")

try:
    find_student(101)
    find_student(105)
except StudentNotFoundError as error:
    print("Error:", error)


# Challenge 5: Exception Inheritance

class ApplicationError(Exception):
    pass


class InvalidUserError(ApplicationError):
    pass


class InvalidPasswordError(ApplicationError):
    pass


print("\nChallenge 5: Exception Inheritance")

try:
    raise InvalidUserError("Invalid username.")
except ApplicationError as error:
    print("Application Error:", error)

try:
    raise InvalidPasswordError("Invalid password.")
except ApplicationError as error:
    print("Application Error:", error)


# Challenge 6: Student Result System

class InvalidStudentMarksError(Exception):
    pass


def calculate_result(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidStudentMarksError(
                "Each subject mark must be between 0 and 100."
            )

    total = sum(marks)
    average = total / len(marks)

    print("Total marks:", total)
    print("Average marks:", average)


print("\nChallenge 6: Student Result System")

try:
    subject_marks = [85, 90, 78]
    calculate_result(subject_marks)
except InvalidStudentMarksError as error:
    print("Error:", error)


# Challenge 7: Banking Transaction System

class InsufficientTransferBalanceError(Exception):
    pass


def transfer(balance, amount):
    if amount > balance:
        raise InsufficientTransferBalanceError(
            "Transfer amount exceeds available balance."
        )

    remaining_balance = balance - amount
    print("Transfer successful!")
    print("Remaining balance:", remaining_balance)


print("\nChallenge 7: Banking Transaction System")

try:
    transfer(10000, 3000)
    transfer(5000, 7000)
except InsufficientTransferBalanceError as error:
    print("Error:", error)