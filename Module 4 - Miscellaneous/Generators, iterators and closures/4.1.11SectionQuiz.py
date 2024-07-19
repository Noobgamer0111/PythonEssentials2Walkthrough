# Question 1: What is the expected output of the following code?
class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Yes, we know that y is not always considered a vowel.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]

vowels = Vowels()
for v in vowels:
    print(v, end=' ')
# Expected output: a e i o u y

# Question 2: Write a lambda function, setting the least significant bit of its integer argument,
# and apply it to the map() function to produce the string 1 3 3 5 on the console.
any_list = [1, 2, 3, 4]
even_list = list # Complete the line here:
print(even_list)

# Expected line to write:
list(map(lambda n: n | 1, any_list))
# Expected solution and output:
any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)
# Output: [1, 3, 3, 5]

# Question 3: What is the expected output of the following code?
def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
 
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))

# Expected output: And*Now*for*Something*Completely*Different