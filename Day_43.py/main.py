
# Main file: importing custom modules

import math_utils
import greetings

print(math_utils.add(10, 5))
print(math_utils.subtract(10, 5))
print(math_utils.multiply(10, 5))
print(math_utils.divide(10, 5))

print("PI:", math_utils.PI)

print(greetings.greet("Lalitendra"))
print(greetings.welcome("Student"))



from mypackage.calculator import square, cube
from mypackage.messages import show_message

print(square(5))
print(cube(3))

show_message()

