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

print(float("1.3"))
# Answer: 1.3

class Class:
    def __init__(self, val=0):
        pass
# Answer: object = Class(1, 2)

class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v)
# Answer: 3

class A:
    A = 1
    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))
# Answer: False

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(A, C))
# Answer: False

class A:
    def __init__(self, v):
        self.__a = v + 1

a = A(0)
print(a.__a)
# Answer: AttributeError

class A:
    def __init__(self, v):
        pass

a = A(1)
print(hasattr(a, 'A'))
# Answer: False

class A:
    def a(self):
        print("a")

class B:
    def a(self):
        print("b")

class C(B, A):
    def c(self):
        self.a()

o = C()
o.c()
# Answer: b

try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))
# Answer: 3

def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in my_fun(2):
    print(x, end='')
# Answer: +++++++

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x, end='')
# Answer: abc

def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())
# Answer: ***

q = s.read(1)
# Answer: one character from the stream.

for x in open('file', 'rt'):
    print(x)
# Answer: reads file line by line.

number = [0, 2, 7, 9, 10]
# Insert line of code here.
print(list(foo))

# To get output: [0, 4, 49, 81, 100]
# Answer:
foo = map(lambda num: num ** 2, number)

numbers = [i*i for in range(5)]
# Insert line of code here.
print(foo)
# To get output: [1, 9]
# Answer:
