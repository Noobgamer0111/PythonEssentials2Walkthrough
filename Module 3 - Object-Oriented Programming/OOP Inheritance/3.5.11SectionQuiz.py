# Initial code for the quiz:
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


# Question 1:Question 1: The declaration of the Snake class is given below. 
# Enrich the class with a method named increment(), adding 1 to the __victims property.
# Add in "print(rocky) print(luna)" to see the output.

# Answer:

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

# Expected output: 
# Collie says: Woof! Don't run away, Little Lamb!
# Dobermann says: Woof! Stay where you are, Mister Intruder!

# Question 2: What is the expected output of the following piece of code?

# print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
# print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

# Answer: 
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
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

# Expected output:
# True False
# False True

# Question 3: What is the expected output of the following piece of code?

# print(luna is luna, rocky is luna)
# print(rocky.kennel)

# Answer:
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
print(luna is luna, rocky is luna)
print(rocky.kennel)

# Expected output:
# True False
# 2

# Question 4: Define a SheepDog's subclass called LowlandDog, and equip it with an __str__() method
# overidding an inherited method of the same name. The new dog's __str__() should return the string
# "Woof! I don't like mountains!".

# Answer:

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

class LowlandDog(SheepDog):
	def __str__(self):
		return Dog.__str__(self) + " I don't like mountains!"
 
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
