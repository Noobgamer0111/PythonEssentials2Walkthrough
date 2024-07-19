# Demonstrate closure in Python 
def outer(par):
    loc = par
 
 
var = 1
outer(var)
 
# print(par)
# print(loc)

# Output:
# Traceback (most recent call last): Nameerror : name 'par' is not defined
# Traceback (most recent call last): Nameerror : name 'loc' is not defined

# Making modifications as necessary

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())
    
# Expected output:
# 1

# Declaring a closure function must also be invoked in the same manner.
def outer(par):
    loc = par
 
    def inner():
        return loc
    return inner
 
 
var = 1
fun = outer(var)
print(fun())

# Expected output:
# 1

# Declaring a closure function with arbitrary parameters:
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
    
# Expected output:
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# And so on...

