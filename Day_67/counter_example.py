from collections import Counter

fruits = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]

result = Counter(fruits)

print(result)

print("Apple count:", result["apple"])
print("Banana count:", result["banana"])