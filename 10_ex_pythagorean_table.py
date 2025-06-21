# Multiplication Table

print("MULTIPLICATION TABLE")
print("")

N = int(input("Enter N"))  # Set the number of tables to print

for i in range(1, N + 1):  # Loop from 1 to N, excluding the last number from the range
    print("Multiplication table of ", i)  # Print the multiplication table for the current number
    for j in range(1, 11):  # Loop through numbers from 1 to 10, excluding 11
        print(i, "*", j, "=", i * j)  # Print the product of i and j
    print("")  # Create a space between each table

# Creating a matrix table
print("MULTIPLICATION TABLE")
print("")

N = int(input("Enter N"))  # Set the number of tables to print

# Create the header row for the columns
print("*", end="\t")
for i in range(1, N + 1):
    print(i, end="\t")
print("")

# Create a line of dashes for separating the header from the table
for i in range(1, N * 9):
    print("-", end="")
print("")

# Create the rows for the multiplication table
for i in range(1, N + 1):
    print(i, end="\t")
    for j in range(1, 11):
        print(i * j, end="\t")
    print("")