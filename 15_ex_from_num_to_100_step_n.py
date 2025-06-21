# From Number to 100 with Step n

print("FROM NUMBER TO 100 WITH STEP N")

num = 100

incr = -1

while incr < 0 or incr > 100:
# The loop asks the user to enter an increment between 1 and 100.
# If < 0 or > 100, it will continue asking.
    incr = int(input("Enter increment value: "))
    
while num > 100 - incr:
# Enter the value of the number to be incremented, which should be
# less than the suggested number. Otherwise, it will not exit the loop.
    num = int(input("Enter number <" + str(100 - incr) + ": "))

i = 0
# Initialize the counter

while num < 100:

    num += incr

    i += 1
# As long as num is less than 100, it adds incr and increases the counter i.

print("To reach or exceed 100, it takes: ", i, "additions with ", incr)