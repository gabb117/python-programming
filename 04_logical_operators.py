# Logical Operators

# 'and' operator (x > 0 and y > 0)
# false and false = false --- e.g., x = -1, y = -1
# false and true  = false --- e.g., x = -1, y = 5
# true and false  = false --- e.g., x = 5, y = -1
# true and true   = true  --- e.g., x = 5, y = 5

# 'or' operator (x > 0 or y > 0)
# false or false = false --- e.g., x = -1, y = -1
# false or true  = true  --- e.g., x = -1, y = 1
# true or false  = true  --- e.g., x = 1, y = -1
# true or true   = true  --- e.g., x = 1, y = 1

# 'not' operator (not(x > 0))
# Example: if x > 0 is false, then not(x > 0) is true (e.g., x = -1)
#          if x > 0 is true, then not(x > 0) is false (e.g., x = 1)


# Logical operators for numerical intervals
number = int(input("Enter a numeric value: "))

# Using nested if statements to check if the value is within the interval [10, 20]
if number >= 10:
    if number <= 20:
        print("The value is within the interval")
else:
    print("The value is not within the interval")


# Using a combined condition to check if the value is within the interval [10, 20]
if number >= 10 and number <= 20:
    print("The value is within the interval")
else:
    print("The value is not within the interval")

# Flag false = condition not met
# Flag true  = condition met