#exceptions: when we ourselves set the type of error 
# to return if it occurs

a = 2
b = 0

try:
    print(a/b)
    #impossible to divide a number by zero
except ZeroDivisionError:
    print("Attention, division by zero")

try:
    infile = open('copy.txt','r')
    #copy.text does not exist

except FileNotFoundError:
    print("The file does not exist")

def main():

    try:
        infile = open('copy.txt','r')

        total = 0
        counter = 0

        for riga in infile:
            grade = int(infile.rstrip('\n'))
            total = total + grade
            counter = counter + 1

        print("The average of grades is: ", float(total)/counter)

    except ZeroDivisionError:
        print("Attention, division by zero")

    except FileNotFoundError:
        print("The file does not exist")

    except ValueError:
        print("non-numerical vote")

    except:
        print("an error occurred")
 


main()