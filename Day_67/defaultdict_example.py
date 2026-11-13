from collections import defaultdict

student_marks = defaultdict(list)

student_marks["Rahul"].append(85)
student_marks["Rahul"].append(90)

student_marks["Arjun"].append(80)

print(dict(student_marks))

# Example 2: Counting occurrences of words using defaultdict
from collections import defaultdict

word_count = defaultdict(int)

words = ["python", "java", "python", "c", "java", "python"]

for word in words:
    word_count[word] += 1

print(dict(word_count))