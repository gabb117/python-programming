# while loop (pre-test loop)
# before executing an iteration, the condition is checked
# the while loop continues as long as the condition is true;
# as soon as it becomes false, the loop stops

a = 1

while a <= 10:
    print(a)
    a = a + 1
# prints the value of 'a', incremented by 1, until it reaches 10 and stops
# because the condition is a <= 10, once a becomes 11, the condition is false


# using a flag to control the while loop
# if false, the loop continues
# if true, the loop terminates
# the initial value of the flag in this case must be set to false

stop = False  # variable set to False

while not stop:  # so, while it's not True
    name = input("Enter your name: ")  # enter a string
    if name == "stop":  # if the input is "stop"
        stop = True     # the flag becomes True, and the loop ends
    else:
        print("Welcome ", name)


# for loop
# numerically controlled loop
# iterates for a defined number of times
# on each iteration, the loop variable takes the value from the set
# of numbers or elements provided in the loop declaration

for i in [1, 2, 3, 4, 5]:
    print(i)  # prints 1 2 3 4 5


# range() function
# simplifies the use of 'for' loops with numerical sequences
# range returns an iterable object that generates a sequence of values

# if one argument is given, it is used as the upper limit
for i in range(10):
    print(i)  # prints 0 to 9, excluding 10


# if two arguments are given, they represent the lower and upper bounds
for i in range(1, 10):
    print(i)  # prints 1 to 9, includes lower but excludes upper bound


# if three arguments are given, the third is the step (increment value)
for i in range(1, 10, 2):
    print(i)  # prints 1 3 5 7 9, starting from 1 and incrementing by 2


# negative step: counts backwards
for i in range(1, -10, -1):
    print(i)  # prints 1 to -9, excluding -10


# sometimes the exact number of iterations is not known
# ask the user how far to count
end = int(input("Up to what number do you want to count? "))
for i in range(1, end + 1):
    print(i)  # counts up to the number the user wants