from constants import pv_initials


def menu():
    print()
    print("MENU")
    print("1. Enter a new home to manage")
    print("2. Delete a house under management")
    print("3. Find a house by price")
    print("4. Print all houses under management")
    print("5. Exit the program")
    print()

def ask_number(prompt,type_n):
    correct = False
    while not correct:
        try:
            if type_n == "float":
                n = float(input(prompt))
            else:
                n = int(input(prompt))
            correct = True

        except:
            print("\tERROR! Invalid value entered")
    return n

def ask_y_n(prompt): #ask in input a string value for yes or no
    correct = False
    while not correct:
        s = (input(prompt)).upper()#makes characters uppercase 
        if s in ['Y','N']:
            correct = True
    return s

def ask_pc():
    valid_digits = 0
    digits = "0123456789"

    while valid_digits != 5:
        valid_digits = 0
        s = input("Postal code [five digits]? ")
        if len(s) == 5:
            for c in s:
                if c in digits:
                    valid_digits += 1
                
        if len(s) != 5 or valid_digits != 5:
            print("\tERROR! Invalid value entered")
        
    return s 
    

def ask_pv_initial():
    correct = False
    while not correct:
        i_pv = (input("Province code? ")).upper()
        if i_pv in pv_initials:
            correct = True
        else:
            print("\tERROR! Initial not valid")

    return i_pv


def ask_min_max(): #requires the minimum and maximum price values ​​as input to search for houses of interest
    min_price = ask_number("Enter minimun price: ", "float")
    max_price = ask_number("Enter maximum price: ", "float")
    min_p = min(min_price, max_price) #the entered values ​​are reordered to avoid confusion between minimum and maximum
    max_p = max(min_price, max_price)
    return min_p,max_p

def ask_info_house(code): #allows you to request all the data of the owner and the house as input
    try:
        name = input("Owner's name: ")
        surname = input("Owner's surname: ")
        t = input("Telephone number: ")
        c = input("Mobile phone: ")
        p = Person(name,surname,t,c)

        #numeric requests
        price = ask_number("Enter house's price: ", "float")
        rooms = ask_number("Enter number of rooms: ", "int")
        sm = ask_number("Enter house's square metes", "float")

        #[Y/N] type requests
        elevator = ask_y_n("Does the house have a lift [Y/N] ? ")
        condominium = ask_y_n("Is the house located in a condominium [Y/N] ? ")
        garage = ask_y_n("Does the house have a garage [Y/N] ? ")

        #postal code request
        pc = ask_pc()

        #type string request
        address = input("House address? ")
        town_hall = input("Name of municipality ")
        pv = ask_pv_initial()

        h = House(code,price,rooms,sm,elevator,condominium,garage,address,pc,town_hall,pv,p)

        return h 

    except Exception as error:
        print("ERROR: ", error)
        return 1

