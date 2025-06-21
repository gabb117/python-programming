# Quadratic equation

import math

print("QUADRATIC EQUATION")
print("Given a quadratic equation in the form ax^2 + bx + c = 0 with a != 0")

a = 0

while a == 0:
    a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

delta = b**2 - 4*a*c

if abs(delta) < 0.0001:  # Checks if delta is approximately zero
    x1 = -b / (2 * a)
    print("The real and coincident solutions are x1 = x2 = ", x1)
elif delta < 0:  # Checks if delta is less than zero
    print("The equation has no real solutions")
else:  # Checks if delta is greater than zero, having ruled out the other cases
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("The real and distinct solutions are: ")
    print("x1 = ", x1)
    print("x2 = ", x2)

# abs(delta) < 0.0001 checks if the absolute value of delta is very close to zero
# abs(delta) ignores the sign (positive or negative)
# The 0.0001 is a small tolerance threshold, as sometimes with decimals
# (floats), rounding errors occur. In this case, delta might not be exactly zero
# but 0.0001. Anything smaller than 0.0001 is considered zero.