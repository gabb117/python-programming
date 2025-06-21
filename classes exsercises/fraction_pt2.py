#fraction part 2

import fraction as Fc

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
            val = (Fc.Fraction(f1_n, f1_d)).calculate_value()
            print("\t>> Value of fraction: ",format(val,",.3f"))

        elif choise == SIMPL:
            f1_n = ask_numerator("Numerator: ")
            f1_d = ask_denominator("Denominator [!=0]: ")
            f = (Fc.Fraction(f1_n, f1_d)).simplify()
            print("\t>> Fraction reduced to lowest terms: ",f)
            
        elif choise in [SUM, DIFF, MULT, DIV]:
            f1_n = ask_numerator("Numerator: ")
            f1_d = ask_denominator("Denominator [!=0]: ")
            f2_n = ask_numerator("Numerator: ")
            f2_d = ask_denominator("Denominator [!=0]: ")
            f1 = Fc.Fraction(f1_n, f1_d)
            f2 = Fc.Fraction(f2_n, f2_d)
            if choise == SUM:
                f = f1.sum(f2)
            elif choise == DIFF:
                f = f1.diff(f2)
            elif choise == MULT:
                f = f1.multiplication(f2)
            elif choise == DIV:
                f = f1.division(f2)
            print("\t The result of the fraction is: ",f)

        elif choise ==  QUIT:
            print("Exit the program")
        else:
            print("Attention, this option is not available")


main()

