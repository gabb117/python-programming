#julias's coffee warehouse
#using excepions


import os

ADD = 1
VIEW = 2
SEARCH = 3
MODIFY = 4
DELETE = 5
QUIT = 6 

def add(filename,descr,quant):
    try:
        outfile = open(filename,'a')
        outfile.write(descr+'\n')
        outfile.write(str(quant)+'\n')
        print(descr + "saved in the file "+ filename)
        outfile.close()

    except ValueError:
        print("Invalid numeric quantity")
        infile.close()

    except:
        print("An error occurred")
        infile.close()



def view(filename):
    try:
        infile = open(filename,'r')
        descr = infile.readline()
    
        while descr != '':
            quant = float(infile.readline())
            descr = descr.rstrip('\n')

            print("Description: "+ descr +" - quantity: "+str(quant)+"kg")
            descr = infile.readline()
    
    except FileNotFoundError:
        print("File does not exist, check file name")

    except ValueError:
        print("Invalid numeric quantity")
        infile.close()

    except:
        print("An error occurred")
        infile.close()

    else:
        infile.close



def search(filename,descr):

    try:
    
        found = False 

        infile = open(filename,'r')

        d = infile.readline()
        while d != '' and found == False:
            quant = float(infile.readline())
            d = d.rstrip('\n')

            if descr == d:
                print("Coffee found - Description:  "+descr+" - quantity: "+str(quant)+" kg")
                found = True

            d = infile.readline()
    
        infile.close()

        if not found:
            print(descr+" not found in file")

    except FileNotFoundError:
        print("File does not exist, check file name")

    except ValueError:
        print("Invalid numeric quantity")
        infile.close()

    except:
        print("An error occurred")
        infile.close()

    else:
        infile.close



def modify(filename,descr,new_quant):
    try:

        found = False

        infile = open(filename,'r')
        tempfile = open('temp.txt','w')

        d = infile.readline()

        while d != '':
            quant = float(infile.readline())
            d = d.rstrip('\n')

            if descr == d:
                tempfile.write(d+'\n')
                tempfile.write(str(new_quant)+'\n')
        
            else:
                tempfile.write(d+'\n')
                tempfile.write(str(quant)+'\n')
        
            d = infile.readline()

        infile.close()
        tempfile.close()

        os.remove(filename)
        os.rename('temp.txt',filename)

        if found:
            print(descr+" updated in the file")

        else:
            print(descr+" not found in the file. File not uploaded")

    except FileNotFoundError:
        print("File does not exist, check file name")

    except ValueError:
        print("Invalid numeric quantity")
        infile.close()

    except:
        print("An error occurred")
        infile.close()

    else:
        infile.close



def delete(filename,descr):
    try:

        found = False

        infile = open(filename,'r')
        tempfile = open('temp.txt','w')

        d = infile.readline()

        while d != '':
            quant = float(infile.readline())
            d = d.rstrip('\n')

            if descr != d:
                tempfile.write(d+'\n')
                tempfile.write(str(quant)+'\n')

            else:
                found = True
        
            d = infile.readline()

        infile.close()
        tempfile.close()

        os.remove(filename)
        os.rename('temp.txt',filename)

        if found:
            print(descr+" deleted from file. File uploaded")

        else:
            print(descr+" not found in the file. File not uploaded")

    except FileNotFoundError:
        print("File does not exist, check file name")

    except ValueError:
        print("Invalid numeric quantity")
        infile.close()

    except:
        print("An error occurred")
        infile.close()

    else:
        infile.close




def show_menu():
    print("\n\tMENU")
    print("1. Add coffee")
    print("2. Show coffee warehouse")
    print("3. Search coffee's quantity in warehouse")
    print("4. Modify coffee's quantity in warehouse")
    print("5. Delete coffee")
    print("6. Exit the program")




def main():
    
    choise = 0
    filename = "coffee.txt"

    while choise != QUIT:
        show_menu()
        choise = int(input("Select an option (1-6):\t"))
        print()

        if choise == ADD:
            descr = input("Coffee description: ")
            quant = float(input("Quantity (in kg) : "))
            add(filename,descr,quant)
            print()
        
        elif choise == VIEW:
            view(filename)
            print()

        elif choise == SEARCH:
            descr = input("Description of the coffee to search for: ")
            print()
            search(filename,descr)
            print()

        elif choise == MODIFY:
            descr = input("Coffee description: ")
            quant = float(input("Enter new quantity (in kg): "))
            modify(filename,descr,quant)
            print()

        elif choise == DELETE:
            descr = input("Coffee description: ")
            delete(filename,descr)
            print()

        elif choise == QUIT:
            print("Exit the program...")

        else:
            print("Error, invalid choise")



main()