# if statement

number = int(input("Enter a number: "))

if number > 0:
    print("The number is greater than zero")
else:
    print("The number is less than or equal to zero")


# String comparison
if "claude" == "Claude":
    print("Strings are equal")
else:
    print("Strings are not equal")


# Nested if
# Find the largest of three stored numbers

a = 3
b = 2
c = 1

if a > b:
    if a > c:
        print("a is the largest")
    else:
        print("c is the largest")
else:
    if b > c:
        print("b is the largest")
    else:
        print("c is the largest")


# if-elif-else structure

grade = int(input("Enter the grade: "))

if grade >= 9:
    print("Grade: Excellent")
elif grade >= 8:
    print("Grade: Good")
elif grade >= 7:
    print("Grade: Fair")
elif grade >= 6:
    print("Grade: Pass")
else:
    print("Grade: Fail")