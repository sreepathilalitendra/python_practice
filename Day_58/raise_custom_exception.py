
# Day 58: Raise Custom Exception

class InvalidMarksError(Exception):
    pass


def check_marks(marks):

    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    print("Valid marks:", marks)


try:

    check_marks(85)
    check_marks(120)

except InvalidMarksError as error:
    print("Error:", error)
