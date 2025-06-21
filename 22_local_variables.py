#local variables

def printer():
    a = 7 #local variable of printer's function 
    print("a =",a)

def main():
    a = 3 #local variable of main's function 
    printer()
    print("a =",a)

main()
#a = 7
#a = 3
#Prints two values of "a", due to the fact that each "a" is a local 
#variable of a function, so they will not have the same value.