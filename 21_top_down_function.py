# Hypothesis where the power operator does not exist

def power(a, b):
    c = 1  # initialized to 1 because it's the neutral value for multiplication
    for i in range(b):  # the loop repeats for the number of times specified by the exponent
        c *= a  # c is multiplied by a for each iteration of the loop
    return c  # returns the value of c once the loop is finished

def main():
    a = int(input("Enter the base: "))  # input the base number
    b = int(input("Enter the exponent: "))  # input the exponent value
    print(power(a, b))

main()