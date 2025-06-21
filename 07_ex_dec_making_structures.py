# Exercise 1
# Comparison between two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

if num1 > num2:
    print("num1 is greater:", num1)
elif num1 == num2:
    print("num1 and num2 are equal:", num1)
else:
    print("num2 is greater:", num2)

# Simple and optimized version
if num1 > num2:
    print("num1 is greater:", num1)
else:
    if num1 == num2:
        print("num1 and num2 are equal:", num1)
    else:
        print("num2 is greater:", num2)

# Version with nested if

# Exercise 2
# Comparison between three numbers
if num1 > num2:
    if num1 > num3:
        print("num1 is the greatest:", num1)
    elif num1 < num3:
        print("num3 is the greatest:", num3)
    else:
        print("num1 and num3 are the greatest:", num1)
elif num2 > num1:
    if num2 > num3:
        print("num2 is the greatest:", num2)
    elif num2 < num3:
        print("num3 is the greatest:", num3)
    else:
        print("num2 and num3 are the greatest:", num2)
elif num1 > num3:  # if num1 and num2 are equal
    print("num1 and num2 are the greatest:", num1)
elif num3 > num1:
    print("num3 is the greatest:", num3)
else:
    print("num1, num2, and num3 are all equal:", num1)