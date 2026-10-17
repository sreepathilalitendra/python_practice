# CHALLENGE 1: Find the product from 1 to n

def product_numbers(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0 or number == 1:
        return 1

    return number * product_numbers(number - 1)


print(product_numbers(5))


# CHALLENGE 2: Count digits

def count_digits(number):
    number = abs(number)

    if number < 10:
        return 1

    return 1 + count_digits(number // 10)


print(count_digits(12345))


# CHALLENGE 3: Find the greatest common divisor

def gcd(a, b):
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(48, 18))


# CHALLENGE 4: Check whether a string is a palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("madam"))
print(is_palindrome("python"))


# CHALLENGE 5: Find the sum of a list recursively

def list_sum(numbers):
    if not numbers:
        return 0

    return numbers[0] + list_sum(numbers[1:])


print(list_sum([10, 20, 30, 40]))


# CHALLENGE 6: Find the maximum in a list recursively

def find_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    if len(numbers) == 1:
        return numbers[0]

    maximum_of_rest = find_max(numbers[1:])

    if numbers[0] > maximum_of_rest:
        return numbers[0]

    return maximum_of_rest


print(find_max([10, 45, 20, 80, 30]))


# CHALLENGE 7: Convert a decimal number to binary

def to_binary(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number < 2:
        return str(number)

    return to_binary(number // 2) + str(number % 2)


print(to_binary(10))


# CHALLENGE 8: Calculate the sum of even numbers from 1 to n

def sum_even(number):
    if number <= 1:
        return 0

    if number % 2 == 0:
        return number + sum_even(number - 2)

    return sum_even(number - 1)


print(sum_even(10))