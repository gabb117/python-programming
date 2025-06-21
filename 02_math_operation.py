# Mathematical operations

a = 10
b = 7

print("Result a + b =", a + b)
print("Result a - b =", a - b)
print("Result a * b =", a * b)
print("Result a / b =", a / b)
print("Result a // b =", a // b)

# One slash returns a float result (floating-point division)
print(type(a / b))
# Two slashes return an integer result (floor division)
print(type(a // b))


grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

average_grade = (grade1 + grade2 + grade3) / 3

print("The average grade is:", average_grade)

# Exponent operator (**)
# "x ** y"

# Modulo operator (%)
# Returns the remainder

4 % 2
5 % 2
# Typically used to convert time/distance or check even/odd numbers


# Time calculations

# Receive total number of seconds as input
total_seconds = float(input("Enter the number of seconds: "))

# Calculate the number of hours
hours = total_seconds // 3600  # One hour = 3600 seconds

# Calculate the remaining number of minutes
minutes = (total_seconds // 60) % 60

# Calculate the remaining number of seconds
seconds = total_seconds % 60

# Print the result
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


# Operator precedence:
# 1. Parentheses
# 2. Exponents (**)
# 3. Multiplication (*), division (/ and //), and modulo (%)
# 4. Addition (+) and subtraction (-)


# Operations with mixed types

result = 3 * 7
print(type(result))
# Between two integers → result is 'int'

result = 3 * 7.0
print(type(result))
# Between int and float → result is 'float'


# Type casting functions

x = 3.4
y = int(x)
print(y)
# Result: 3

a = 3
b = float(a)
print(b)
# Result: 3.0


# Line continuation character (\)

name = 'Gabriele'
print("My name is", \
      name)