
import logging

# Example 1: Basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

# Example 2: Different logging levels
logging.debug("This is a debug message")
logging.info("Python program started")
logging.warning("This is a warning message")
logging.error("An error occurred")
logging.critical("Critical problem detected")


# Example 3: Logging with variables
name = "Lalitendra"
age = 18

logging.info("Student name: %s", name)
logging.info("Student age: %d", age)


# Example 4: Logging calculations
a = 20
b = 10

result = a + b

logging.info("First number: %d", a)
logging.info("Second number: %d", b)
logging.info("Addition result: %d", result)


# Example 5: Logging into a file
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "application.log",
    encoding="utf-8"
)

file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
)

file_logger.addHandler(file_handler)

file_logger.info("Application started")
file_logger.warning("Sample warning")
file_logger.error("Sample error")

file_handler.close()
file_logger.removeHandler(file_handler)


# Example 6: Logging an exception
try:
    number = 10 / 0

except ZeroDivisionError:
    logging.exception("Division operation failed")


# Example 7: Custom logger
custom_logger = logging.getLogger("MyApplication")
custom_logger.setLevel(logging.INFO)

custom_logger.info("Custom logger started")
custom_logger.warning("Custom warning message")


# Example 8: Student management logging project
student_logger = logging.getLogger("StudentManagement")
student_logger.setLevel(logging.INFO)

student_handler = logging.FileHandler(
    "student.log",
    encoding="utf-8"
)

student_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
)

student_logger.addHandler(student_handler)

student_logger.info("Student record created")
student_logger.info("Student details updated")
student_logger.warning("Student record needs verification")

student_handler.close()
student_logger.removeHandler(student_handler)

print("Logging examples completed successfully")
