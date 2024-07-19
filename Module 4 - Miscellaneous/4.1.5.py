# Lambda Function
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# Expected Output:
# 4 4 1 1 0 0 1 1 4 4