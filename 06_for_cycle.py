# Loop from 0 to 9, then add 1 to print 1 through 10
for i in range(10):
    print(i + 1)

# Loop from 5 to 15 (range includes the start, excludes the end)
for i in range(5, 16):
    print(i)

# Start at 2, go up to 20 with a step of 2 (even numbers only)
for i in range(2, 21, 2):
    print(i)

# Start at 10, decrease by 1 each time until reaching 1
for i in range(10, 0, -1):
    print(i)

# Initialize accumulator to 0
total = 0
# Loop from 1 to 100 and add each number to total
for i in range(1, 101):
    total += i
# Print the final result
print("Total sum:", total)

# Ask the user for a number
n = int(input("Enter a number: "))
# Multiply the number by values from 1 to 10
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Ask the user for a word
word = input("Enter a word: ")
# Loop through each letter in the word
for letter in word:
    print(letter)