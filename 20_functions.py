#functions

#void function
def housing_data():
    print("Abbey Road")
    print("St John’s Wood")
    print("London")

#value-returning function
def somma(a,b):
    return a+b

def double(val1):
    r = val1 * val1 
    print("The double is: ",r)


#main function
def main():
    housing_data()
    print("The result of the sum is: ",somma(3,2))
    double(somma(3,2))

#call of the function
main()

def reset(value):
    value = 0 #temporary cop of variable "value"
    print("Value = ", value)

def main():
    value = 10
    reset(value)
    print("Value = ", value)
#the function maintains the value of variable "value" unchanged within the function
#and create a temporary copy inside the reset function

main()

#value = 0
#value = 10
#so we will have two different outputs