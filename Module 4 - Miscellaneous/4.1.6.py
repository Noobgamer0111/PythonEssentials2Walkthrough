# Using the lambda function, write a function that prints the value of a polynomial for a given value of x. The polynomial is f(x) = 2x^2 - 4x + 2. Print the value of the polynomial for x = -2, -1, 0, 1, and 2.
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
    