from collections import deque

numbers = deque([10, 20, 30])

# Add elements
numbers.append(40)
numbers.appendleft(5)

print("After adding:", numbers)

# Remove elements
numbers.pop()
numbers.popleft()

print("After removing:", numbers)