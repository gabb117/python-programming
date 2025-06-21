#OOP (Object-Oriented Programming)
#encapsulation - information hiding
#heredity
#polymorphism

#To every object belongs to a "class" 
#Class is the code that specifies the attributes and methods of a particular object
#For Instance we define an object created by the class with the characteristics defined by the class
#For a given class there can be multiple instances
#Has "attributes" (variables)
#The "state" defines the set of values of attributes
#Performs actions or functions called methods that modify its state
#Set of methods of an object is called "interface"
#To access the object's attributes from outside, methods are used.

#e.g. automobile CLASS

#The ATTRIBUTES of the car class will be: engine capacity, speed, make, model

#The class' METHODS are: accelerate(),brake(),turnOff().They generally act on the attributes of the class
#METHOD accelerate()will change the speed ATTRIBUTE over time

#an INSTANCE or OBJECT of the automobile class maintains all the methods and provides a value for the attributes:
#engine cpacity = 3902, speed = 130km, make = Ferrari, model = 488 GTB
# dot notation = used to reference object attributes and methods

import random

class Coin:  #the first letter of the class must always be capitalized
    
    def __init__ (self):  #standard method of initializing an object
        self.sideup = "Heads"  #"upside" is the attribute of class coin
        #Once the object is initialized, it will see the coin with the "Head" side up

    def flip(self): # simulates the toss of a coin
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
    
    def get_sideup(self): #will return the current value of the up side of the coin
        return self.sideup
    
    
    def __str__(self): #show the object's status
        return "Output value: " + self.sideup

def main():
    c = Coin()
    c.flip()
    print(c)

main()


#public = self.sideup
#Accessible from anywhere (inside or outside the class). In Python, all attributes are public by default.

#private = self.__sideup
#Accessible from within the class,use two underscores __ in front of the name to indicate a private attribute.
#Getter/Setter can be defined for all attributes 
#Getter method (get_coin()) = returns the value of the class attribute without modifying it
#Setter method (set_color()) = stores or modifies the value of an attribute, also carrying out checks and/or processing if necessary

#UML diagram layout
# ______________
#|    Coin     | Class name
#|_____________|
#| __sideup    | Attributes list
#|_____________|
#| __init__()  | 
#| flip()      | Methods list
#| get_sideup()|
#| __str__()   |
#|_____________|

c = Coin() #create an object "c" in the class Coin()
print(c.get_sideup()) #give "c" the method "get_sideup"
for i in range(5): 
    c.flip() #iterate five time the function or method flip() with object "c"
    print(c.get_sideup())
#"sideup" is an attribute of "c"