
from constants import *
from file_manager import save_house, load_houses
from menu import *
from house import House







def main():
    agency = dict()
    load_houses(agency)
    modify = False
    choise = 0
    while choise != QUIT:
        menu()

        choise = int(input("Enter your choise: "))

        if choise == ADD_HOUSE:
            code = (input("Enter unique house code: ")).upper()
            if code not in agency:
                c = ask_info_house(code)
                if c != 1:
                    agency[code] = c
                    modify = True
            else:
                print("Code already present!")
        elif choise == DELETE_HOUSE:
            code = input(("Enter the code of the house to delete")).upper()
            print()
            if code in agency:
                del agency[code]
                modify = True
                print("the house with the code " + code + " has been deleted!")
            else:
                print("Incorrect unique house code")
            print()

        elif choise == FIND_HOUSE:#find houses in a range of price
            print()
            if len(agency) == 0:
                print("No house under management")
            else:
                min_p, max_p = ask_min_max()
                n_case = 0
                for key in agency:
                    if agency[key].get_price() >= min_p and agency[key].get_price() <= max_p:
                        print(agency[key])
                        print()
                        n_case += 1
                    
                if n_case == 0:
                    print("No houses with price between: " + str(min_p) + "€ and " + str(max_p)+ "\n")

        elif choise == IN_MANAGEMENT_HOUSE:
            print()
            if len(agency) == 0:
                print("No house in management")
            else:
                for key in agency:
                    print(agency[key])
                    print()

        elif choise != QUIT:
            print("ERROR: invalid choise")

    if modify:
        print("Current house storages")
        save_house(agency)
    print("Program finished")

    import os
    print("📂 File saved in:", os.path.abspath(NAME_FILE))


main()
