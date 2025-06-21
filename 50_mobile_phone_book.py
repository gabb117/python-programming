SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def search(numbers):
    name = input("Enter a name: ")
    print(numbers.get(name, "Not found"))


def add(numbers):
    name = input("Enter a name: ")

    if name not in numbers:
        num = input("Enter a phone number: ")
        numbers[name] = num
    else:
        print("Entry already exists")


def change(numbers):
    name = input("Enter a name: ")

    if name in numbers:
        num = input("Enter a new phone number: ")
        numbers[name] = num
    else:
        print("Name not present in the address book")


def delete(numbers):
    name = input("Enter a name: ")

    if name in numbers:
        del numbers[name]
    else:
        print("Name not present in the address book")


def menu():
    print()
    print("Address book")
    print("------------")
    print("1. Search a phone number")
    print("2. Add a phone number")
    print("3. Change a phone number")
    print("4. Delete a phone number")
    print("5. Exit the program")
    print()
    choise = int(input("Enter your choise: "))

    while choise < SEARCH or choise > QUIT:        #choice within the range 1-5
        choise = int(input("Enter your choise: "))
    
    return choise


def main():
    numbers = dict() #empty address book

    choice = 0       #intentionally invalid choice

    while choice != QUIT:
        choice = menu()

        if choice == SEARCH:
            search(numbers)
        elif choice == ADD:
            add(numbers)
        elif choice == CHANGE:
            change(numbers)
        elif choice == DELETE:
            delete(numbers)

main()