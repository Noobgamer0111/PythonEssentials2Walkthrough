# Scenario
class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"
 
 
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"
 
 
class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"
 
 
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")

print(rocky)
print(luna)
# Question 1:Question 1: The declaration of the Snake class is given below. 
# Enrich the class with a method named increment(), adding 1 to the __victims property.

