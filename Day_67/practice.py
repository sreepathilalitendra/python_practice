
from collections import Counter, defaultdict, namedtuple, deque
numbers = [10, 20, 10, 30, 20, 10, 40, 30]

number_count = Counter(numbers)

print("CHALLENGE 1: NUMBER FREQUENCY")
print(number_count)



students = [
    ("Rahul", "Python"),
    ("Arjun", "Java"),
    ("Kiran", "Python"),
    ("Ravi", "Java"),
    ("Suman", "C")
]

subject_groups = defaultdict(list)

for name, subject in students:
    subject_groups[subject].append(name)

print("\nCHALLENGE 2: STUDENT GROUPS")

for subject, names in subject_groups.items():
    print(subject, ":", names)



Employee = namedtuple("Employee", ["name", "age", "salary"])

employee1 = Employee("Rahul", 25, 30000)

print("\nCHALLENGE 3: EMPLOYEE DETAILS")
print("Name:", employee1.name)
print("Age:", employee1.age)
print("Salary:", employee1.salary)



student_queue = deque(["Rahul", "Arjun", "Kiran"])

student_queue.append("Ravi")
student_queue.appendleft("Suman")

print("\nCHALLENGE 4: STUDENT QUEUE")
print("Original Queue:", student_queue)

student_queue.pop()
student_queue.popleft()

print("Updated Queue:", student_queue)



sentence = "python is easy and python is powerful and python is popular"

words = sentence.split()

word_count = Counter(words)

print("\nCHALLENGE 5: WORD FREQUENCY")
print(word_count)

print("Top 3 Common Words:")

for word, count in word_count.most_common(3):
    print(word, ":", count)


Student = namedtuple("Student", ["name", "subject", "marks"])

student_records = [
    Student("Rahul", "Python", 85),
    Student("Arjun", "Java", 90),
    Student("Kiran", "Python", 85),
    Student("Ravi", "Java", 75),
    Student("Suman", "Python", 90)
]

# Count marks frequency

marks = [student.marks for student in student_records]

marks_count = Counter(marks)

print("\nCHALLENGE 6: STUDENT MARKS ANALYZER")

print("\nMarks Frequency:")

for mark, count in marks_count.items():
    print(mark, ":", count)


# Group students by subject

subject_groups = defaultdict(list)

for student in student_records:
    subject_groups[student.subject].append(student.name)

print("\nStudents by Subject:")

for subject, names in subject_groups.items():
    print(subject, ":", names)


# Display top 2 marks

print("\nTop 2 Marks:")

for mark, count in marks_count.most_common(2):
    print(mark, ":", count, "student(s)")


# Process students using deque

student_queue = deque(student_records)

print("\nStudent Processing Queue:")

while student_queue:
    student = student_queue.popleft()
    print(student.name, "-", student.marks)
