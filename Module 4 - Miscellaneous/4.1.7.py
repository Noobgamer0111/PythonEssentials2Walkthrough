# Show how lambdas can be used with the map() function.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
    
# Expected output:
# [1, 2, 4, 8, 16]
# 1 4 16 64 256