# Questions/Answers for the final exam of the Python Essentials 2 course.

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

print(__name__)
# Answer: __main__

from a.b import c
# Answer:  entity c from module b from package a.

try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")
# Answer: a

for line in open('text.txt', 'rt'):
# Answer: Invalid. Open is a non-iterable object.

try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
# Answer: Syntax error.

assert var != 0
# Answer: Program stops when var == 0.

x = "\\\\"
print(len(x))
# Answer: 2

x = "\\\"
print(len(x))
# Answer: Will cause an error

print(chr(ord('p') + 2))
# Answer: r

