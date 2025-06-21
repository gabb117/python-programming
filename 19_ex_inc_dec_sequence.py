# GROWING AND DECREASING SUBSEQUENCE

print("GROWING AND DECREASING SUBSEQUENCE")  # Title

# Initialization of flags and counters
is_increasing = 0       # flag: 1 if currently in an increasing sequence
is_decreasing = 0       # flag: 1 if currently in a decreasing sequence
max_increasing_len = 0  # longest increasing subsequence found
max_decreasing_len = 0  # longest decreasing subsequence found
current_inc_len = 0     # current increasing subsequence length
current_dec_len = 0     # current decreasing subsequence length
sequence_length = 0     # total number of values in the sequence

# Ask the user for the sequence length (must be greater than 1)
while sequence_length <= 1:
    sequence_length = int(input("Enter the length of the sequence: "))

# Read the first number
previous_number = int(input("Enter number no. 1: "))

# Loop through the remaining numbers
for i in range(1, sequence_length):
    current_number = int(input("Enter number no. " + str(i + 1) + ": "))

    # Check for increasing sequence
    if current_number >= previous_number:
        if is_increasing == 1:
            current_inc_len += 1  # continue the sequence
        else:
            is_increasing = 1
            current_inc_len = 2   # start a new sequence
    else:
        if is_increasing == 1:
            if current_inc_len > max_increasing_len:
                max_increasing_len = current_inc_len
            is_increasing = 0  # sequence interrupted

    # Check for decreasing sequence
    if current_number <= previous_number:
        if is_decreasing == 1:
            current_dec_len += 1  # continue the sequence
        else:
            is_decreasing = 1
            current_dec_len = 2   # start a new sequence
    else:
        if is_decreasing == 1:
            if current_dec_len > max_decreasing_len:
                max_decreasing_len = current_dec_len
            is_decreasing = 0  # sequence interrupted

    # Move to next comparison
    previous_number = current_number

# Final check: if the sequence ended on an increasing or decreasing run
if is_increasing == 1 and current_inc_len > max_increasing_len:
    max_increasing_len = current_inc_len

if is_decreasing == 1 and current_dec_len > max_decreasing_len:
    max_decreasing_len = current_dec_len

# Print results
print("The longest increasing subsequence is", max_increasing_len, "numbers long")
print("Which corresponds to", float(max_increasing_len) * 100 / sequence_length, "% of the sequence")

print("The longest decreasing subsequence is", max_decreasing_len, "numbers long")
print("Which corresponds to", float(max_decreasing_len) * 100 / sequence_length, "% of the sequence")