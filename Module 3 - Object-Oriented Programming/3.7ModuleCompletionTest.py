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
# A3: A.__init__(self)
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
# Explanation: The hasattr() function returns True if a specified object has some specified 
# attribute. The function takes two arguments:the name of the object whose attribute is to
# be tested, and the name of the attribute.
# The code returns True because class A has the attribute A.

# Question 8: What will be the result of executing the following code?
class A:
     def __init__(self):
        pass

a = A(1)
print(hasattr(a,'A'))
# A8: it will raise an exception
# The code will raise a TypeError exception, because the __init__() method takes only one argument
# (self), but two positional arguments are passed upon object a instantiation (self and 1).
# The print() function is not executed.

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
# Explanation: The customized __str__() method is called because the print() function is 
# invoked on the object o. As there is no __str__() method within the C class,
# the string printed to the console (i.e. b) is produced within the B class,
# which means that the __str__() method has been inherited by the C class.

# Question 10: What will be the result of executing the following code?
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C,A))
# A10: True
# Explanation: The code will print True to the console because the result of the test 
# issubclass(C, A) evaluates to True. The function issubclass(C, A) checks whether class C 
# is a subclass of class A, and returns True when the test is positive, and False otherwise.

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
# The code will not raise an exception because it is consistent with the Method Resolution Order (MRO).
# The code will output b to the console, because class C inherits from classes B and A respectively,
# and if any of the subclasses defines a method of the same name as existing in the superclass
# – in this case, class B defines the method def a(self): 
# – the new name overrides any of the previous instances of the name (in this case, print('b') overrides print('a')).
# As a result, even though the c method defined in class C makes a reference to the a method defined in class A, the invocation o.c() results in printing b, not a to the screen.

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
# Explanation: The code will print a to the screen, because the class named first in the 
# multiple inheritance path (in this case, class C(A, B):) passes its attribute value to the child class
# (in this case, class C). The code will not raise an exception, 
# because it’s compatible with the MRO rules.

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
# Let’s analyze the code:
# Class A sets the v variable to 2
# Class B, which inherits after class A, sets the v variable to 1
# Class C inherits from class B
# An object o is created from class C, and the v variable is accessed and its value is printed to the screen.
# Because the subclass B defines a class variable of the same name as existing in the superclass A,
# the old v value is overridden by the new one, and inherited by the C class.

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
# A14: it will print bcac
# Let’s analyze the code:
# An f function is defined, and it takes one parameter x.
# The function is called two times:
# - first invocation with 1 passed as an argument, in which case no exception is raised in the try 
# block, so the else block is executed, printing b to the screen. Because the finally block is always executed no matter what happens earlier,
# c is printed to the console.
# - second invocation with 0 passed as an argument, in which case an exception is raised (division by zero is illegal,
# so the except block is executed) and a is printed to the console. 
# Again, because the finally block is always executed, c is printed to the screen a second time.
# The four strings are “glued” together using the end keyword parameter.

# Question 15: What will be the result of executing the following code?
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))
# A15: it will print 3
# The except branch is executed and intercepts the object carrying information about the exception. 
# The args property, which is a tuple, gathers all arguments passed to the Exception class constructor: 1, 2, and 3.
# The len function computes the length of the tuple (i.e. 3), which is printed to the console.

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
# A16: it will print ex
# Let’s analyze this code snippet:
# First, the try block raises an Ex Exception with the ex string as its argument.
# Then, the Ex Exception receives the ex string in the msg variable.
# Afterwards, the replicated string msg + msg is passed on to the superclass. 
# However, the content of the msg variable is stored in self.args.
# Finally, the raised exception will fall under the Ex Exception. 
# It prints the content of the e variable in the console, which is ex.

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
# Let’s analyze this code snippet:

# First, a for loop using the x variable iterates through the already defined I() generator.
# The generator class initializes the self.s = 'abc' and self.i = 0 variables within the constructor.
# The __next__ method compares if the value in i is equal to the length of s.
# Since it is not, v is assigned the first character of s, which is a, i is incremented by one,
# v is returned and printed in the console.
# The end=’’ argument in the print function will prevent new lines, so all the outputs will be shown on the same line.
# The iteration continues for the remaining characters in s. The b and c characters are also printed in the console.
# When the condition self.i == len(self.s) becomes true, a StopIteration is raised. This terminates the execution.