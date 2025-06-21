#heredity

import math

class Geometric_figure:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def set_x(self,x):
        self.__x = x

    def get_x(self):
        return x 

    def set_y(self,y):
        self.__y = y 

    def get_y(self):
        return y  

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"



class Circle(Geometric_figure):

    def __init__(self,x,y,r):
        Geometric_figure.__init__(self,x,y)
        self.__r = r

    def set_r(self,r):
        self.__r = r

    def get_r(self):
        return r 

    def calculate_perimeter(self) :
        return 2 * math.pi * self.__r

    def calculate_area(self):
        return self.__r * (math.pi ** 2)

    def __str__(self):
        return "Radius circle " + str(self.__r) + " centered in " + Geometric_figure.__str__(self)


def main():
    c = Circle(0,0,1)
    print(c)
    print("The perimeter of the circle is: ",format(c.calculate_perimeter(),",.2f"))
    print("The area of circle is: ",format(c.calculate_area(),",.2f"))

main()


#UML diagram layout                  ___________________                   
# Heredity base                      |                 |                               
# ______________                     |            ______________
#| Geometric f.| Class name          |            |    Circle   | Class name
#|_____________|                     |            |_____________|
#| __x  __y    | Attributes list     |            | __r         | Attributes list 
#|_____________|                     |            |_____________| It hereditate also __x and __y attribute
#| __init__()  |                     |            | __init__()  |
#|set_x/y(x)(y)| Methods list        |            | set_r(r)    | Methods list
#|get_x/y()    |                     |            | get_r()     |
#| __str__()   |                     |            |calculate.p()|
#|_____________|                     |            |calculate.a()|
#       ^                            |            |__str__()    |
#       |____________________________|            |_____________|
