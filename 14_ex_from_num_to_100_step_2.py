# From Number to 100 with Step 2

print("FROM NUMBER TO 100")
n = 100
while n > 98:

    n = int(input("Enter number: "))

i = 0  # Initialize i for counting

while n < 100:  # When n is >= 100, the loop ends

    n += 2  # n is increased by 2 units until it reaches or exceeds 100

    i += 1  # Keeps track of the number of times 2 is added to n to reach 100

print("To reach or exceed 100, it takes: ", i, "additions of 2")

