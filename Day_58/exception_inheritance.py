
# Day 58: Exception Inheritance

class StudentError(Exception):
    pass


class StudentNotFoundError(StudentError):
    pass


class InvalidStudentDataError(StudentError):
    pass


def find_student(student_id):

    if student_id <= 0:
        raise InvalidStudentDataError(
            "Student ID must be positive."
        )

    if student_id != 101:
        raise StudentNotFoundError(
            "Student not found."
        )

    return "Lalitendra"


try:

    student = find_student(101)
    print("Student found:", student)

    student = find_student(105)
    print("Student found:", student)

except StudentError as error:
    print("Student Error:", error)
