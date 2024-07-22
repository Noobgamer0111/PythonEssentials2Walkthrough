def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
 
 
for x in fun(2):
    print(x, end='');

# What is the output of this code?
def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())

# Output:
# +++++++********

import calendar

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")

