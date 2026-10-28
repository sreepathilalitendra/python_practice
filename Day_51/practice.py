# Challenge 1: Price formatting

price = 4599.9876

print(f"Price: {price:.2f}")


# Challenge 2: Percentage formatting

score = 0.92345

print(f"Score: {score:.2%}")


# Challenge 3: Number formatting

salary = 1250000

print(f"Salary: {salary:,}")


# Challenge 4: Text alignment

brand = "CODEMONOLITH"

print(f"{brand:<20}")
print(f"{brand:>20}")
print(f"{brand:^20}")


# Challenge 5: Student report

student_name = "Lalitendra"
marks = 425
total_marks = 500

percentage = marks / total_marks * 100

print("\n--- Student Report ---")
print(f"Name       : {student_name}")
print(f"Marks      : {marks}/{total_marks}")
print(f"Percentage : {percentage:.2f}%")
