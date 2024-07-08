# Question 1: Which of the Python class properties are instance variables and which are class variables? Which of them are private?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False
 
# population and victims are class variables, while length and __venomous are instance variables (the latter is also private).

# Question 2: You're going to negate the __venomous property of the version_3 object, ignoring the fact that the property is private. How will you do this?

# input: version_3 = Python()
version_3 = Python()
version_3._Python__venomous = not version_3._Python__venomous

# Question 3: Write an expression which checks if the version_2 object contains an instance property named constrictor (yes, constrictor!).

hasattr(version_3, 'constrictor')
    