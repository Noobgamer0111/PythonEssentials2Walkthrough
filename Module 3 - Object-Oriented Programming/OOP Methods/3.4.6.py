# 3.4.6 Section Quiz

# Question 1: The declaration of the Snake class is given below.
# Enrich the class with a method named increment(), adding 1 to the victims property.

class Snake:
    def __init__(self):
        self.victims = 0

# Answer 1:  

class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1

# Question 2: Redefine the Snake class constructor so that is has a parameter to
# initialize the victims field with a value passed to the object during construction.

# Answer 2:
class Snake:
    def __init__(self, victims):
        self.victims = victims

# Question 3: Can you predict the output of the following code?

class Snake:
    pass

class Python(Snake):
    pass

print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be', Python.__name__)

# Answer 3:

# Python is a Snake
# Snake can be Python