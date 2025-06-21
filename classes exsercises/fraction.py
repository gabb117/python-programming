#fractions part 1
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
        f3 = Fraction(self.__n * f2.__n, self.__d * f2.__d)
        return f3.simplify() #return multiplication fraction

    def division(self,f2):
        f3 = Fraction(self.__n * f2.__d, self.__d * f2.__n)
        return f3.simplify() #return division fraction

