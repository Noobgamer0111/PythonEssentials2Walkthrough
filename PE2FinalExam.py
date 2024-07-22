from mod import fun
# Answer: fun()

import math
print(dir(math))
# Answer:
# A list of all the entities in the math module

# file a.py
print("a", end='')

# file b.py
import a
print("b", end='')

# file c.py
print("c", end='')
import a
import b

# Answer: cab