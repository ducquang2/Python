# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]

print(*product(a, b))
# Example:
# a = [1, 3]
# b = [5, 6]
# product(a, b) =  [(1, 5), (1, 6), (3, 5), (3, 6)]
# print(*product(a, b)) -> unpack product(a, b) = print((1, 5), (1, 6), (3, 5), (3, 6))