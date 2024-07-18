# Question 1: A data structure described as LIFO is actually a:
# A1: stack
# Explanation: A stack is a data structure that follows the Last In First Out (LIFO) principle.
# and LIFO is a method for handling data structures in which the first element added is the last
# one to be processed, and the last element is processed first.

# Question 2: If the class’s constructor is declared as below, which one of the assignments is valid?
class Class:
    def __init__(self):
        pass
# A2: object = Class()
# Explanation: The object = Class() assignment creates an object of class Class, and the __init__ method is automatically 
# called when that object is created. The __init__ constructor has the obligatory parameter self, no attributes,
# and it does not do anything because a placeholder statement – pass – is executed.
# The object = Class(object) assignment will result in a TypeError exception, because the
# __init__() method should take only one positional argument (self), not two (self and object).
# The object = Class(self) assignment will result in a NameError exception, because the name
# self has not been defined anywhere.
# The object = Class assignment declares the object variable and assigns Class to it,
# but it does not initialize an object of class Class.

# Question 3: If there is a superclass named A and a subclass named B,
# which one of the presented invocations should you put instead of the comment?
class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        # Put selected line here.
        self.b = 2
# A3: A.__init__(1)
# The example shows a superclass named A, which defines its own constructor.
# The A class is then used as a base to create a subclass named B, which defines
# its own constructor. The B class constructor should now invoke the constructor
# from the A class, which can be done like this: A.__init__(self).

# Question 4: What will be the effect of running the following code?
class A:
    def __init__(self,v):
        self.__a = v + 1

a = A(0)
print(a.__a)
# A4: The code will raise an AttributeError exception.
# Explanation: The following code will result in the AttributeError exception, because the A object does not have the attribute __a.
# The __a variable is a private instance variable, and an attempt to access or modify it from outside the class 
# will result in an AttributeError.
# Modifying the private attribute __a and changing it to public (a) will result in the following output: 1.

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
# Explanation: Let’s analyze the code:
# The A class constructor creates an instance variable named v equal to the default value passed to the constructor’s parameter v, which is 1.
# The set method creates its own v variable, and returns the value passed to it.
# The a object is created, and the set method is called, which returns the v value equal to 1 + 1.
# The result 2 is printed to the console.

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
# Explanation: Let’s analyze the code:
# The first line of the class A definition sets the variable named X to 0. Because X is a class variable, it exists in just one copy and is stored outside any object.
# The class constructor sets the instance variable Y with the v parameter’s value, which defaults to 0.
# The class constructor sets another instance variable equal to the value of the class variable X incremented by the value assigned to v.
# When the a object is created, the X class variable stores 0.
# When the b object is created, the X class variable is incremented with the argument sent, so now X=1.
# When the c object is created, the X class variable is incremented with the argument sent, so now X=3.
# When invoking the print function, 3 is printed in the console.

# Question 7: What will be the output of the following code?
class A:
    A = 1

print(hasattr(A,'A'))
# A7: True
# Explanation: The hasattr() function returns True if a specified object has some specified attribute. The function takes two arguments: 
# the name of the object whose attribute is to be tested, and the name of the attribute.
# The code returns True because class A has the attribute A.

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
# A17: it will print abc