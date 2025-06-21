#fractions
#To see the UML diagram go to --> fraction_UML.puml

class Fraction:

    def __init__(self,num,den): #constructor of a fraction
        # The abs() function returns the absolute value, removing the negative sign if present,
        # since the denominator cannot have a negative number or be equal to zero.        
        if num * den < 0:       #sign management
            self.__n = - abs(num) #in this case we can understand in fraction has positive or negative sign
        else:                     
            self.__n = abs(num)
        self.__d = abs(den) #denominator always > 0

    def __str__(self):  #displays a fraction type object
        return(str(self.__n) + "/" + str(self.__d))

    def __GCD(self,x,y): #greatest common divisor (MCD massimo comune divisore)
        if y == 0: #if y = 0,  GCD is x
            gcd = x
        else:      
            while x % y != 0: # Euclid's algorithm
                rest = x % y
                x = y
                y = rest
            gcd = y
            return(gcd)
        #Otherwise, calculate x \mod y (the remainder of the division),replace x with y and y with (x mod y)
        #repeat until y = 0
    def calculate_value(self): #calculate float value of a fraction
        return float(self.__n/self.__d)

    def simplify(self): #simplify a fraction if is possible
        a = abs(self.__n)
        b = abs(self.__d)
        x = max(a,b)
        y = min(a,b)

        #calculate GCM between numerator and denominator
        gcd = self.__GCD(x,y)

        f3 = Fraction(int(self.__n / gcd),int(self.__d / gcd))
        return f3

    def sum(self,f2):
        f3 = Fraction(self.__n * f2.__d + f2.__n * self.__d, self.__d * f2.__d)
        return f3.simplify() #return sum fraction

    def diff(self,f2):
        f3 = Fraction(self.__n * f2.__d - f2.__n * self.__d, self.__d * f2.__d)
        return f3.simplify() #return difference fraction

    def multiplication(self,f2):
        f3 = Fraction(self.__n * f2.__n, self.__d * fe.__d)
        return f3.simplify() #return multiplication fraction

    def division(self,f2):
        f3 = Fraction(self.__n * f2.__d, self.__d * f2.__n)
        return f3.simplify() #return division fraction

import Fraction as Fz

VALUE = 1
SIMPL = 2
SUM = 3
DIFF = 4
MULT = 5
DIV = 6
QUIT = 7

def ask_numerator(prompt):
    valid = False
    while not valid:
        try:
            numerator = int(input(prompt))
            valid = True
        except:
            print("Error! this value is not valid ")
    return numerator

def ask_denominator(prompt):
    denominator = 0
    while denominator == 0:
        try:
            denominator = int(input(prompt))
        except:
            print("Error! this value is not valid ")
    return denominator

def show_menu():
    print("\n\tMENU")
    print("1. Calculate the value of a fraction")
    print("2. Simplify a fraction")
    print("3. Calculate the sum of two fractions")
    print("4. Calculate the difference of two fractions")
    print("5. Calculate the multiplication of two fractions")
    print("6. Calculate the division of two fractions")
    print("7. Quit")

def main():
    choise = 0
    while choise != QUIT:
        show_menu()
        choise = int(input("\nSelect one of proposed option (1-7):\t "))

        if choise == VALUE:
            f1_n = ask_numerator("Numerator: ")
            f1_d = ask_denominator("Denominator [!=0]: ")
            val = (Fz.Fraction(f1_n, f1_d)).calculate_value()
            print("\t>> Value of fraction: ",format(val,",.3f"))

        elif choise == SIMPL:
            f1_n = ask_numerator("Numerator: ")
            f1_d = ask_denominator("Denominator [!=0]: ")
            f = (Fz.Fraction(f1_n, f1_d)).simplify()
            print("\t>> Fraction reduced to lowest terms: ",f)
            

