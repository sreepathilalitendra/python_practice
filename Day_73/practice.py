
import logging

# Challenge 1: Display all five logging levels
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    force=True
)

logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")


# Challenge 2: Display INFO and higher
info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.INFO)

print("\nINFO and higher levels:")
info_logger.info("Information message")
info_logger.warning("Warning message")
info_logger.error("Error message")
info_logger.critical("Critical message")


# Challenge 3: Log name and course
logging.info("Student name: Lalitendra")
logging.info("Course: Diploma CSE")


# Challenge 4: Log multiplication result
a = 12
b = 5

result = a * b

logging.info("Multiplication: %d * %d = %d", a, b, result)


# Challenge 5: Save logs into student.log
student_logger = logging.getLogger("student_logger")
student_logger.setLevel(logging.DEBUG)
student_logger.propagate = False

student_handler = logging.FileHandler(
    "student.log",
    encoding="utf-8"
)

student_handler.setFormatter(
    logging.Formatter("%(levelname)s: %(message)s")
)

student_logger.addHandler(student_handler)

student_logger.info("Student registered")
student_logger.warning("Student details need verification")
student_logger.error("Student record error")

student_handler.close()
student_logger.removeHandler(student_handler)

print("\nStudent logs saved")


# Challenge 6: Add timestamps to log messages
timestamp_logger = logging.getLogger("timestamp_logger")
timestamp_logger.setLevel(logging.INFO)
timestamp_logger.propagate = False

timestamp_handler = logging.FileHandler(
    "timestamp.log",
    encoding="utf-8"
)

timestamp_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
)

timestamp_logger.addHandler(timestamp_handler)

timestamp_logger.info("Application started")
timestamp_logger.info("Timestamp logging example")

timestamp_handler.close()
timestamp_logger.removeHandler(timestamp_handler)


# Challenge 7: Record an exception
try:
    number = 10 / 0

except ZeroDivisionError:
    logging.exception("Division error occurred")


# Challenge 8: Create CodeMonolith custom logger
code_logger = logging.getLogger("CodeMonolith")
code_logger.setLevel(logging.INFO)

code_handler = logging.StreamHandler()

code_handler.setFormatter(
    logging.Formatter(
        "CodeMonolith - %(levelname)s: %(message)s"
    )
)

code_logger.addHandler(code_handler)

code_logger.info("CodeMonolith application started")
code_logger.warning("Sample warning message")

code_handler.close()
code_logger.removeHandler(code_handler)


# Challenge 9: Student Registration Logger
registration_logger = logging.getLogger("registration")
registration_logger.setLevel(logging.INFO)
registration_logger.propagate = False

registration_handler = logging.FileHandler(
    "registration.log",
    encoding="utf-8"
)

registration_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
)

registration_logger.addHandler(registration_handler)

registration_logger.info("New student registered")
registration_logger.info("Student name: Lalitendra")
registration_logger.info("Course: Diploma CSE")
registration_logger.warning("Verification pending")

registration_handler.close()
registration_logger.removeHandler(registration_handler)


# Challenge 10: Mini Application Logger
app_logger = logging.getLogger("mini_application")
app_logger.setLevel(logging.DEBUG)
app_logger.propagate = False

app_handler = logging.FileHandler(
    "application_activity.log",
    encoding="utf-8"
)

app_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
)

app_logger.addHandler(app_handler)

app_logger.info("User logged in")
app_logger.info("User viewed dashboard")
app_logger.warning("Session is about to expire")
app_logger.info("User logged out")
app_logger.error("Sample application error")

app_handler.close()
app_logger.removeHandler(app_handler)

print("\nAll Day 73 challenges completed!")
