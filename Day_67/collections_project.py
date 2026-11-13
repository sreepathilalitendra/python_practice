from collections import Counter, defaultdict, namedtuple, deque


# 1. Student records using namedtuple

Student = namedtuple("Student", ["name", "marks"])

students = [
    Student("Rahul", 85),
    Student("Arjun", 90),
    Student("Kiran", 85),
    Student("Ravi", 75),
    Student("Suman", 90)
]


# 2. Count marks using Counter

marks = [student.marks for student in students]

mark_count = Counter(marks)

print("Marks Frequency:")
print(mark_count)


# 3. Group students by marks using defaultdict

student_groups = defaultdict(list)

for student in students:
    student_groups[student.marks].append(student.name)

print("\nStudent Groups:")

for mark, names in student_groups.items():
    print(mark, ":", names)


# 4. Manage student queue using deque

student_queue = deque(["Rahul", "Arjun", "Kiran"])

student_queue.append("Ravi")

print("\nStudent Queue:")
print(student_queue)

first_student = student_queue.popleft()

print("Processed Student:", first_student)
print("Remaining Queue:", student_queue)