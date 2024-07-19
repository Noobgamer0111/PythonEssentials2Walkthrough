# 1. An iterator is an object of a class providing at least two methods (not counting the constructor):
# __iter__() is invoked once when the iterator is created and returns the iterator's object itself;
# __next__() is invoked to provide the next iteration's value and raises the StopIteration exception when the iteration comes to an end.

# 2. The yield statement can be used only inside functions. The yield statement suspends function
# execution and causes the function to return the yield's argument as a result.
# Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator
# (i.e. in a context that requires a series of values, like a for loop).

# 3. A conditional expression is an expression built using the if-else operator. For example:

print(True if 0 >= 0 else False)
 # Outputs: True

# 4. A list comprehension becomes a generator when used inside parentheses (used inside brackets,
# it produces a regular list). For example:

for x in (el * 2 for el in range(5)):
    print(x)
 
# Outputs: True.

# 4. A lambda function is a tool for creating anonymous functions. For example:
def foo(x, f):
    return f(x)
 
print(foo(9, lambda x: x ** 0.5))
# Outputs: 3.0

# 5. The map(fun, list) function creates a copy of a list argument, and applies the fun function
# to all of its elements, returning a generator that provides the new list content element by element.
# For example:
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)
# Outputs: ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor']

# 6. The filter(fun, list) function creates a copy of those list elements, 
# which cause the fun function to return True. The function's result is a generator providing the 
# new list content element by element.
# For example:
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)
# Outputs: ['Python', 'Monty']

# 7. A closure is a technique which allows the storing of values in spite of the fact that the
# context in which they have been created does not exist anymore. For example:
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
 
    def inner(str):
        return tg + str + tg2
    return inner
 
b_tag = tag('<b>')
print(b_tag('Monty Python'))
 
# Outputs: <b>Monty Python</b>