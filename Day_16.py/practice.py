# Challenge 1
# Create a tuple containing 5 programming languages
# and print the tuple.

languages = ("Python", "Java", "C", "C++", "JavaScript")
print(languages)


# Challenge 2
# Print each programming language using a for loop.

for language in languages:
    print(language)


# Challenge 3
# Print the first and last item using indexing.

print(languages[0])
print(languages[-1])


# Challenge 4
# Print the length of the tuple.

print(len(languages))


# Challenge 5
# Check whether "Python" exists in the tuple using in.

print("Python" in languages)


# Challenge 6 🔥
# Create a tuple containing 5 numbers
# and print only the numbers using a for loop.

numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# Challenge 7 🔥
# Create a tuple:
# ("Python", "Java", "C", "C++", "JavaScript")
#
# Print:
# First item
# Last item
# First 3 items using slicing

languages = ("Python", "Java", "C", "C++", "JavaScript")
print(languages[0])
print(languages[-1])
print(languages[0:3])
