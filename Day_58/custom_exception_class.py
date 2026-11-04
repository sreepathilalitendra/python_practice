
# Day 58: Custom Exception with Constructor

class InsufficientBalanceError(Exception):

    def __init__(self, balance, amount):

        self.balance = balance
        self.amount = amount

        message = (
            f"Insufficient balance! "
            f"Available: {balance}, Requested: {amount}"
        )

        super().__init__(message)


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(balance, amount)

    return balance - amount


try:

    remaining_balance = withdraw(5000, 7000)

    print("Remaining balance:", remaining_balance)

except InsufficientBalanceError as error:

    print("Transaction Error:", error)
    print("Available balance:", error.balance)
    print("Requested amount:", error.amount)

class InvalidMarksError(Exception):
    pass


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_result(self):

        if not 0 <= self.marks <= 100:
            raise InvalidMarksError(
                "Marks must be between 0 and 100."
            )

        print("Student:", self.name)
        print("Marks:", self.marks)

        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


try:

    student = Student("Lalitendra", 85)
    student.display_result()

except InvalidMarksError as error:
    print("Error:", error)