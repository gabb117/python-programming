#bank account

class Bank_account:

    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_amount(self):
        return self.__balance

    def __str__(self):
        return "The balance is equal to " + format(self.__balance,",.2f") + "€"

def main():
    #input numeric value of the starting balance
    correct = False #flag 
    while not correct:
        try: #exception handling
            starting_balance = float(input("Enter opening balance: "))
            correct = True
        except:
            print("Error! Non-numeric value entered")

    account = Bank_account(starting_balance)#new current account instance

    #input of the numerical value of the sum to be deposited
    correct = False
    while not correct:
        try: #exception handling
            payment = float(input("Enter payment: "))
            correct = True
        except:
            print("Error! Non-numeric value entered")
        
    account.deposit(payment)
    print(account)

    #input numeric value of amount to withdraw
    correct = False
    while not correct:
        try:
            w = float(input("Enter the quantity to be withdrawn: "))
            correct = True
        except:
            print("Error! Non-numeric value entered")
            
    account.withdraw(w)
    print(account)


main()