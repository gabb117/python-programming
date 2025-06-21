# SUM OF POSITIVES AND NEGATIVES

print("SUM OF POSITIVES AND NEGATIVES")

# Initializing variables to sum the absolute values
pos = 0  # sum of positive numbers
neg = 0  # sum of the absolute values of negative numbers

# Asking the user to input a number
n = int(input("Enter a number (0 to stop): "))

# The loop continues until the user enters 0
while n != 0:
    if n > 0:
        pos += n  # sum of positive numbers
    elif n < 0:
        neg -= n  # equivalent to neg += abs(n), since n is negative

    # Asking for a new number to continue or stop
    n = int(input("Enter a number (0 to stop): "))

# After the loop: comparing the two sums
if pos > neg:
    print("The sum of the absolute values of the positive numbers (", pos, ")")
    print("is greater than the sum of the absolute values of the negative numbers (", neg, ")")
elif neg > pos:
    print("The sum of the absolute values of the negative numbers (", neg, ")")
    print("is greater than the sum of the absolute values of the positive numbers (", pos, ")")
else:
    print("The sum of the absolute values of the negative numbers (", neg, ")")
    print("is equal to the sum of the absolute values of the positive numbers (", pos, ")")