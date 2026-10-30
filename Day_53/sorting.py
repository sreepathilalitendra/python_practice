
# Day 53: Python Sorting Practice

# 1. Sorting numbers using sorted()
numbers = [45, 12, 89, 23, 5]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original list:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)


# 2. Sorting using sort()
marks = [78, 45, 92, 65, 88]

marks.sort()

print("\nSorted marks:", marks)


# 3. Sorting strings alphabetically
names = ["Sree", "Arun", "Kiran", "Balu"]

sorted_names = sorted(names)

print("\nSorted names:", sorted_names)


# 4. Sorting strings by length
words = ["Python", "Java", "C", "JavaScript"]

sorted_words = sorted(words, key=len)

print("\nWords by length:", sorted_words)


# 5. Sorting without considering uppercase/lowercase
fruits = ["banana", "Apple", "cherry", "Mango"]

sorted_fruits = sorted(fruits, key=str.lower)

print("\nSorted fruits:", sorted_fruits)


# 6. Sorting using lambda
students = [
    ("Arun", 85),
    ("Balu", 92),
    ("Kiran", 76),
    ("Sree", 95)
]

sorted_students = sorted(students, key=lambda student: student[1])

print("\nStudents by marks:", sorted_students)


# 7. Sorting dictionaries using a key
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500}
]

sorted_products = sorted(products, key=lambda product: product["price"])

print("\nProducts by price:")

for product in sorted_products:
    print(product["name"], "-", product["price"])
