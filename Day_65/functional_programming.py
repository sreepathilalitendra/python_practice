# Pure function

def square(number):
    return number * number


# Higher-order function

def process_numbers(function, numbers):
    results = []

    for number in numbers:
        results.append(function(number))

    return results


# Original data

numbers = [1, 2, 3, 4, 5]

# Process the list

squared_numbers = process_numbers(square, numbers)


print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)