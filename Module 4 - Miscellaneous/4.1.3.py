# Simple number sequence generator:
def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

# Expected Output:
# 0
# 1
# 2
# 3
# 4

# Generator for powers of two:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(8):
    print(v)

# Expected Output:
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256

# List comprehensions:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

t = [x for x in powers_of_2(5)]
print(t)

# Expected Output:
# [1, 2, 4, 8, 16]

# List function:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

t = list(powers_of_2(3))
print(t)

# Expected Output:
# [1, 2, 4]

# The in operator:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for i in range(20):
    if i in powers_of_2(5):
        print(i)

# Expected Output:
# 1
# 2
# 4
# 8
# 16

# Fibonacci sequence generator:
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)

# Expected Output:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]