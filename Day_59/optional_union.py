# Day 59: Optional and Union Type Hints

from typing import Optional, Union


# Union example
def display_id(student_id: Union[int, str]) -> None:
    print("Student ID:", student_id)


# Optional example
def display_email(email: Optional[str]) -> None:
    if email is None:
        print("Email not provided.")
    else:
        print("Email:", email)


# Calling functions
display_id(101)
display_id("STU102")

display_email("student@example.com")
display_email(None)