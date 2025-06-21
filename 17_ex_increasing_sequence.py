# INCREASING SEQUENCE

print("INCREASING SEQUENCE")

increasing = 0  # flag to check if the sequence is increasing
length = 0  # stores the length of the increasing subsequence
N = 0  # total length of the sequence

# Asking the user to enter the length of the sequence
while N < 1:
    N = int(input("Enter the length of the sequence: "))

# Asking for the first number in the sequence
previous_num = int(input("Enter number n. 1: "))

# Loop to input the rest of the numbers in the sequence
for i in range(1, N):
    current_num = int(input("Enter number n. " + str(i + 1) + " : "))
    
    # Check if the current number is greater than or equal to the previous number
    if current_num >= previous_num:
        if increasing == 1:
            length += 1  # increase the length of the increasing subsequence
        else:
            increasing = 1  # mark the sequence as increasing
            length = 2  # start a new increasing sequence
    previous_num = current_num

# Output the length of the increasing subsequence and its percentage in the whole sequence
print("The increasing sequence contains ", length, " numbers")
print("This corresponds to ", float(length) * 100 / N, " % of the sequence")