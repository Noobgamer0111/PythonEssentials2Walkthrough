# Section Summary:
# 1. A method named __str__() is responsible for converting an object's contents into a 
# (more or less) readable string. You can redefine it if you want your object
# to be able to present itself in a more elegant form. For example:

class Mouse:
    def __init__(self, name):
        self.my_name = name
 
 
    def __str__(self):
        return self.my_name
 
the_mouse = Mouse('mickey')
print(the_mouse) # Prints "mickey".

# 2. A function named issubclass(Class_1, Class_2) is able to determine if Class_1 is a subclass of Class_2. For example:

class Mouse:
    pass
 
class LabMouse(Mouse):
    pass
 
print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse)) # Prints "False True
 
# 3. A function named isinstance(Object, Class) checks if an object comes from an indicated class. For example:

class Mouse:
    pass
 
class LabMouse(Mouse):
    pass
 
mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse)) # Prints "True False".
 
# 4. A operator called is checks if two variables refer to the same object. For example:

class Mouse:
    pass
 
 
mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey) # Prints "False True".
 
# 5. A parameterless function named super() returns a reference to the nearest superclass of the class. For example:

class Mouse:
    def __str__(self):
        return "Mouse"
 
class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()
 
doctor_mouse = LabMouse();
print(doctor_mouse) # Prints "Laboratory Mouse".

# 6. Methods as well as instance and class variables defined in a superclass are automatically inherited by their subclasses. For example:

class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name
 
    def __str__(self):
        return "Hi, my name is " + self.name
 
class LabMouse(Mouse):
    # Remove the line that contains "tpass"
 
    professor_mouse = LabMouse("Professor Mouser")
    print(professor_mouse, Mouse.Population) # Prints "Hi, my name is Professor Mouser 1"
 

# 7. In order to find any object/class property, Python looks for it inside:

# - the object itself;
# - all classes involved in the object's inheritance line from bottom to top;
# - if there is more than one class on a particular inheritance path, Python scans them from left to right;
# - if both of the above fail, the AttributeError exception is raised.

# 8. If any of the subclasses defines a method/class variable/instance variable of the
# same name as existing in the superclass, the new name overrides any of the
# previous instances of the name. For example:

class Mouse:
    def __init__(self, name):
        self.name = name
 
    def __str__(self):
        return "My name is " + self.name
 
class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name
 
mus = AncientMouse("Caesar") # Prints "Meum nomen est Caesar"
print(mus)
 