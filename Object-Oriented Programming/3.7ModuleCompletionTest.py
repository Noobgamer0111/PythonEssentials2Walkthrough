# Question 1: A data structure described as LIFO is actually a:
# A1: stack

# Question 2: If the class’s constructor is declared as below, which one of the assignments is valid?
class Class:
    def __init__(self):
        pass
# A2: object = Class()

# Question 3: If there is a superclass named A and a subclass named B,
# which one of the presented invocations should you put instead of the comment?
class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        # Put selected line here.
        self.b = 2
# A3: .__init__(1)

# Question 4: What will be the effect of running the following code?
class A:
    def __init__(self,v):
        self.__a = v + 1

a = A(0)
print(a.__a)
# A4: The code will raise an AttributeError exception

# Question 5: What will be the output of the following code?
class A:
    def __init__(self,v = 1):
        self.v = v

    def set(self,v):
        self.v = v
        return v

a = A()
print(a.set(a.v + 1))
# A5: 2

# Question 6: What will be the output of the following code?
class A:
    X = 0
    def __init__(self,v = 0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)
print(c.X)
# A6: 3

# Question 7: What will be the output of the following code?
class A:
    A = 1

print(hasattr(A,'A'))
# A7: True

# Question 8: What will be the result of executing the following code?
class A:
     def __init__(self):
        pass

a = A(1)
print(hasattr(a,'A'))
# A8: it will raise an exception

# Question 9: What will be the result of executing the following code?
class A:
    def __str__(self):
        return 'a'

class B(A):
    def __str__(self):
        return 'b'

class C(B):
    pass

o = C()
print(o)
# A9: it will print b

# Question 10: What will be the result of executing the following code?
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C,A))
# A10: True

# Question 11: What will be the result of executing the following code?
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()
# A11: it will print b

# Question 12: What will be the result of executing the following code?\
class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A, B):
    pass

o = C()
print(o)
# A12: it will print a

# Question 13: What will be the result of executing the following code?
class A:
    v = 2

class B(A):
    v = 1

class C(B):
    pass

o = C()
print(o.v)
# A13: it will print 1

# Question 14: What will be the result of executing the following code?
def f(x):
    try:
        x = x / x
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')

f(1)
f(0)
# A14: it will print acac

# Question 15: What will be the result of executing the following code?
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))
# A15: it will print 3

# Question 16: What will be the result of executing the following code?
class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
# A17: it will print ex

# Question 17: What will be the result of executing the following code?
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
    print(x,end='')
# A18: it will print abc