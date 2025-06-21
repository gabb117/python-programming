#overloading functions

def sum (n1,n2,n3):
    return (n1+n2+n3)


def sum (n1,n2):
    return(n1+n2)
#In python the last definition has priority,so the last function sum with two arguments "sum(n1,n2)"
#will be printed while the function with three arguments "sum(n1,n2,n3)" will result as an error having
#found two functions with the samen name

def main():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    n3 = int(input("Enter a number: "))

    print("The sum of two numbers is: ",sum(n1,n2))
    print("The sum of three numbers is: ",sum(n1,n2,n3))

main()
