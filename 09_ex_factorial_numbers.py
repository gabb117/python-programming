# Factorial numbers
# Non-recursive approach, increasing order

print("FACTORIAL")
prod = 1
N = 0
while N <= 1:
    N = int(input("Enter N > 1: "))
for i in range(2, N + 1):
    prod *= i
print("The factorial of N is: ", prod)

# The increasing order will be:
# i=1 --> 1x1=1
# i=2 --> 1x2=2
# i=3 --> 2x3=6
# i=4 --> 6x4=24
# i=5 --> 24x5=120
    
# For example, 5! = 5x4x3x2x1 = 120 or 3! = 3x2x1 = 6
# N! = N x (N-1) x (N-2) x ... x 3 x 2 x 1
# The product of all positive integers from 1 to N
# By convention, 0! = 1
# 10! = 3,628,800

import math
print(math.factorial(5))
# output: 120

# Non-recursive approach, decreasing order
print("FACTORIAL")
prod = 1
N = 0
while N <= 1:
    N = int(input("Enter N > 1: "))
for i in range(N, 1, -1):
    prod *= i
print("The factorial of N is: ", prod)

# The decreasing order will be:
# i=5 --> 1x5=5
# i=4 --> 5x4=20
# i=3 --> 20x3=60
# i=4 --> 60x4=120

n = 3
for i in range(3, n, -1):
    print(i)
# This will not generate a result because there are no numbers to iterate in the range between 3 and 3