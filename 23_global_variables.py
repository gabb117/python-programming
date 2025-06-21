#global variables

#e.g. 1
my_value = 117 #global variable

def show_value():
    print(my_value)

show_value()
#read the value of the global variable my_value outside the function

#e.g. 2
number = 0

def main():
    global number 
    number = int(input("Enter a number: "))
    show_number(number)

def show_number(number):
    print("The number entered is: ",number)

#With the writing "global" before the variable in a function we make
#visible and readable that variable to the other functions or code parts
main()
