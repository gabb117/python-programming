#to see the UML diagram go to file ---|> ClassHierarchy.puml

import ClassHierarchy

CARNIVOROUSMAMMAL = 1
FELINE = 2
CANID = 3
CAT = 4
DOG = 5
QUIT = 6



class CarnivorousMammal:
    description = "Carnivorous mammals are animals equipped with \nspecial teeth, useful for consuming the flesh of other animals;\ncanine teeth that are used to capture prey and tear the flesh"


    def __init__(self,age,life,character,hair,color,race):
        self.__age = age
        self.__life_expectancy = life
        self.__character = character
        self.__hair_type = hair
        self.__fur_color = color
        self.__race = race

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age = age

    def get_life_expectancy(self):
        return self.__life_expectancy

    def set_life_expectancy(self,life):
        self.__life_expectancy = life

    def get_character(self):
        return self.__character

    def set_character(self,character):
        self.__character = character

    def get_hair_type(self):
        return self.__hair_type

    def set_hair(self,hair):
        self.__hair_type = hair

    def get_fur_color(self):
        return self.__fur_color

    def set_color(self,color):
        self.__fur_color = color

    def get_race(self):
        return self.__race

    def set_race(self,race):
        self.__race = race

    def print_legend(self):
        print(CarnivorousMammal.description)

    def communicate(self):
        print("Communication depends on the animal")

    def __str__(self):
        return "\n\tAge: " + str(self.__age) + "\n\tLife expectancy: " + str(self.__life_expectancy) + "\n\tCharacter: " + str(self.__character) + "\n\tHair: " + str(self.__hair_type) + "\n\tColor: " + str(self.__fur_color) + "\n\tRace: " + str(self.__race)

    
class Feline(CarnivorousMammal):
    description = "FELINES: Felines are characterized by agility in hunting,\nwhich includes very large species, including lions and tigers,\nbut also smaller animals such as common cats."

    def __init__(self,age,life,character,hair,color,race,habitat,prey):
        CarnivorousMammal.__init__(self,age,life,character,hair,color,race)#inherits the attributes of the carnivore class
        self.__habitat = habitat
        self.__prey = prey

    def get_habitat(self):
        return self.__habitat

    def set_habitat(self,habitat):
        self.__habitat = habitat

    def get_prey(self):
        return self.__prey

    def set_prey(self,prey):
        self.__prey = prey

    def print_legend(self):
        print(Feline.description)

    def __str__(self):
        return CarnivorousMammal.__str__(self) + "\n\tHabitat: " + str(self.__habitat) + "\n\tPrey: " + str(self.__prey)

    
class Canid(CarnivorousMammal):
    description = "The Canidae family includes carnivores usually with 5 toes on the forelimbs\nand 4 on the hind limbs, with digitigrade feet,\nnon-retractable claws suitable for digging, an elongated head and well-developed teeth\nideal for tearing apart prey."

    def __init__(self,age,life,character,hair,color,race,size,origin):
        CarnivorousMammal.__init__(self,age,life,character,hair,color,race)#inherits the attributes of the carnivore class
        self.__size = size
        self.__origin = origin

    def get_size(self):
        return self.__size

    def set_size(self,size):
        self.__size = size

    def get_origin(self):
        return self.__origin

    def set_origin(self,origin):
        self.__origin = origin

    def print_legend(self):
        print(Canid.description)

    def __str__(self):
        return CarnivorousMammal.__str__(self) + "\n\tSize: " + str(self.__size) + "\n\tOrigin: " + str(self.__origin)


class Cat(Feline):
    description = "The domestic cat, whose domestication began quite recently between 6000 and 10000 AD,\n\tis the most widespread feline."

    def __init__(self,age,life,character,hair,color,race,habitat,prey,name):
        Feline.__init__(self,age,life,character,hair,color,race,habitat,prey)
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def print_legend(self):
        print(Cat.description)

    def communicate(self):
        print("The cat communicates by meowing")

    def __str__(self):
        return Feline.__str__(self) + "\n\tName: " + str(self.__name)



class Dog(Canid):
    description = "The transition from wolf to dog as we see it today took about 5000 generations:\nthe dog was the first animal to be domesticated."

    def __init__(self,age,life,character,hair,color,race,size,origin,name,used_for):
        Canid.__init__(self,age,life,character,hair,color,race,size,origin)
        self.__name = name
        self.__used_for = used_for

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_used_for(self):
        return self.__used_for

    def set_used_for(self,used_for):
        self.__used_for = used_for

    def print_legend(self):
        print(Dog.description)

    def communicate(self):
        print("The dog communicates by barking/howling")

    def __str__(self):
        return Canid.__str__(self) + "\n\tName: " + str(self.__name) + "\n\tUsed for: " + str(self.__used_for)



def display_menu():

    print()
    print("MENU")
    print("1. Create a Carnivorous Mammal")
    print("2. Create a Feline")
    print("3. Create a Canid")
    print("4. Create a Cat")
    print("5. Create a Dog")
    print("6. Exit the program")
    print()

def ask_int(prompt):
    correct = False
    while not correct:
        try:
            n = int(input(prompt))
            correct = True
        except:
            print("ERROR: the value entered is not valid")

    return n

def ask_basic_info():
    a = ask_int("Age: ")
    l = ask_int("Life expectancy: ")
    ch = input("Character: ")
    h = input("Hair type: ")
    col = input("Fur color: ")
    r = input("Race: ")

    return a,l,ch,h,col,r

def ask_feline_info():
    hab = input("Habitat: ")
    pr = input("Prey: ")

    return hab,pr

def ask_canid_info():
    s = input("Size: ")
    o = input("Origin: ")

    return s,o

def display_obj(obj):
    print()
    obj.print_legend()
    print()
    obj.communicate()

def main():
    choice = 0
    obj = 0
    while choice != QUIT:
        display_menu()

        choice = int(input("Enter your choise: "))
        if choice in [CARNIVOROUSMAMMAL,FELINE,CANID,CAT,DOG]:
            a,l,ch,h,col,r = ask_basic_info()

        if choice == CARNIVOROUSMAMMAL:
            obj = CarnivorousMammal(a,l,ch,h,col,r)
            display_obj(obj)

        elif choice == FELINE:
            #habitat,prey
            hab,pr = ask_feline_info()
            obj = Feline(a,l,ch,h,col,r,hab,pr)
            display_obj(obj)

        elif choice == CANID:
            #size,origin
            s,o = ask_canid_info()
            obj = Canid(a,l,ch,h,col,r,s,o)
            display_obj(obj)

        elif choice == CAT:
            #habitat,prey
            hab,pr = ask_feline_info()
            name = input("Enter Cat name: ")
            obj = Cat(a,l,ch,h,col,r,hab,pr,name)
            display_obj(obj)

        elif choice == DOG:
            #name,used for
            s,o = ask_canid_info()
            name = input("Enter Dog name: ")
            u = input("Enter usage of Dog: ")
            obj = Dog(a,l,ch,h,col,r,s,o,name,u)
            display_obj(obj)

        elif choice != QUIT:
            print("ERROR: invalid choise")
            continue

    print("Exit the programm")

main()
