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
