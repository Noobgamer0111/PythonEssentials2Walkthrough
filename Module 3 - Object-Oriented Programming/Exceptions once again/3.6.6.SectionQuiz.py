# Question 1: What is the expected output of the following code?

import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")

# Expected Output: 3.0 fine

# Question 2: What is the expected output of the following code?

import math
 
try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")

# Expected Output: inf the end

# Question 3: What is the expected output of the following code?

import math
 
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)
 
try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')

# Expected Output: Enemy warning! Red alert! High readiness!