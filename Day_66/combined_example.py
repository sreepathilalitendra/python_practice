# Original student data

names = ["Rahul", "Arjun", "Kiran", "Ravi"]

marks = [85, 45, 90, 35]


# map(): Add 5 bonus marks

updated_marks = list(map(lambda mark: mark + 5, marks))


# filter(): Select students with 50 or more marks

passed_marks = list(filter(lambda mark: mark >= 50, updated_marks))


# zip(): Combine names and updated marks

student_data = zip(names, updated_marks)


# enumerate(): Display numbered student records

print("Student Results")

for index, (name, mark) in enumerate(student_data, start=1):
    print(index, name, "-", mark)


print("\nPassed Marks:", passed_marks)