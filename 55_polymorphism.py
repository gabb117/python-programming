# Polymorphism
# The ability to redefine in derived classes the original behaviors of methods inherited from the base class
# Overloading is applied within the same class, while overriding is applied
# within the scope of a class derived from a base class
# Overriding is a polymorphism mechanism by which a derived (child) class 
# redefines a method already present in the base (parent) class
# modifying its behavior.


import math

# Base class
class Geometric_figure:
    # The Geometric_figure class has a method area() that returns only one message.
    def area(self):
        return "Insufficient elements for calculating the area"

# Derived class: class that inherits the base class
class Circle(Geometric_figure):

    def __init__(self, x, y, r): # self. inizialized
        self.x = x  # point x 
        self.y = y  # point y 
        self.__r = r  # radius

    def area(self):
        return math.pi * (self.__r ** 2)  # π * r^2
    # The Circle class, which inherits from Geometric_figure, overrides area() to actually calculate the area of ​​the circle.
    # This is overriding: same method name (area), but different behavior.

def main():
    f = Geometric_figure()
    c = Circle(0, 0, 1)  

    print("Area of geometric figure:", f.area())  
    print("Area of the circle:", c.area()) 
    print(isinstance(c,Circle))      

main()


# Overloading
# It provides the same method or function name but with different parameters
# unlike overriding which provides the same number of parameters

# Common exception of polymorphism:
# AttributeError =  raised when a method receives an object that is not an instance of the correct class

# isinstance() function = determines whether the object is an instance of the class
#  and returns a boolean result True or False
# isistance(object,class)

