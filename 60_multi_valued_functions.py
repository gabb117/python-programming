#exercise on functions
#A focus on functions that return more than one value, unlike C or Java

def math_ops(x,y):
    a = x + y
    b = x - y
    c = x * y
    if y != 0:
        d = x / y
    else:
        d = -1
    
    return a,b,c,d #return more than one value

def main():
    a,b,c,d = math_ops(7,5)

    print("Result of addition: ",a)
    print("Result of subtraction: ",b)
    print("Result of multiplication: ",c)
    print("Result of division: ",d)

main()



import locale #stdlib module that contains functions for internationalizing programs
locale.setlocale(locale.LC_ALL, 'it_IT')
#setlocale set localization parameters with the numeric format of the desired country
#The most used category is LC_ALL which indicates more scopes than the numeric one
#The location is indicated between quotes that identify the country of location

a = locale.atof(input("Enter number: "))
#asks the user to enter a number, which is received as a string and converts a string formatted according to the local convention to a float number.

print(type(a)) #Print the type of the variable a.

print(locale.format_string('%.2f',a))
#Format the number a as a string, using the format '%.2f': decimal number with 2 digits after the decimal point.
#locale.format_string(...) also applies local conventions for thousands and decimal separators.
#The number appears according to the conventional Italian representation


#file exercise
#create a phone number dictionary from a text file

#using a .txt file
def main():
    d = dict() #create a dictionary
    infile = open("telephone_book.txt",'r') #read file .txt
    line = infile.readline() #read a line from the open file and assign it to the line variable.

    #This loop continues as long as there are lines in the file.
    # When readline() reaches the end of the file, it returns '' (empty string), and the loop ends.
    while line != '': 
        key = line.rstrip()
        #key will be the person's name, free from whitespace and any newlines (\n), taken from line which contains the names of each line of the .txt file
        value = infile.readline().rstrip()
        #Reads the next line, which is supposed to be the phone number.Here again we use rstrip() to remove the newline.
        d[key] = value
        #Save the key-value pair in the dictionary of. So d["Fabio Peruzzi"] = "1234".
        line = infile.readline()
        #Move to the next row (the next name) for the next round of the cycle.

    infile.close() # close the file .txt

    print(d)#print the dictionary 
    print("Fabio Peruzzi's number is: ",d["Fabio Peruzzi"])
    #Print only Fabio Peruzzi's number, accessing the key in the dictionary.
main()



#using .csv file
def main():
    d = dict()
    infile = open("telephone_book.csv",'r')

    for line in infile:
        l = line.rstrip().split(',')
        key = l[0]
        value = l[1]
        d[key] = value

    infile.close()

    print(d)
    print("Pina Trobbiani's number is: ",d["Pina Trobbiani"])

main()


#string exercise
#password verify

def valid_password(p):
    has_uppercase = False
    has_lowercase = False
    has_number = False
    if len(p) < 7:
        return False

    for character in p:
        if character.isupper():
            has_uppercase = True
        if character.islower():
            has_lowercase = True
        if character.isdigit():
            has_number = True

    if has_uppercase and has_lowercase and has_number:
        return True
    else:
        return False

def main():
    password = input("Enter new password ")
    if valid_password(password):
        print("The password is valid")
    else:
        print("The password is not valid")

main()


#data structure exercises

#Search complexity plays a fundamental role in the choice of a particular data structure:

#·In lists and tuples the search is linear, in the best case the searched element is the first,
# in the worst case it does not exist in the list.

#list
import time
list1 = list(range(100000000))
search1 = 0
search2 = 200000000
start_time = time.time()
if search1 in list1:
    print(search1,"found in the list")
else:
    print(search1,"not found in the list")
print("Research of",search1,"performed in",format(time.time() - start_time,'.5f'),"seconds")
start_time = time.time()
if search2 in list1:
     print(search2,"found in the list")
else:
    print(search2,"not found in the list")
print("Research of",search2,"performed in",format(time.time() - start_time,'.5f'),"seconds")
print()

#·In sets the search is sublinear, they are not sequences so they do not have an index,
# they can store at most one copy of each element and are excellent for finding and eliminating duplicates

#Time difference between a list and a set
import time
list1 = list(range(100000000))
set1 = set(list1)
search = 200000000
start_time = time.time()
if search in list1:
    print(search,"found in the list")
else:
    print(search,"not found in the list")
print("Research of",search,"performed in",format(time.time() - start_time,'.5f'),"seconds")
start_time = time.time()
if search2 in set1:
     print(search,"found in the set")
else:
    print(search,"not found in the set")
print("Research of",search,"performed in",format(time.time() - start_time,'.5f'),"seconds")
print()


#Removing duplicates from a list using set
list1 = ["house","sea","sea","sea","montain","house","montain"]
print("Initial list: ",list1)
print("Elements in list are: ",len(list1))
newlist = list(set(list1))
#Converts list1 to a set, which does not allow duplicates. It then automatically eliminates all duplicate elements.
#list(...) converts the set back to a list, because a set has no order and does not support indexing like a list.
#newlist = assigns the result to newlist, which will be a list without duplicates.
print("The elements of the list after the transformation into a set are: ",len(newlist))
print("Elaborate list: ",newlist)
print()



#·In dictionaries that create a map between keys and values ​​the search is sublinear, they are excellent for key-value search, 
# all the keys are different inside it and can be of different types

#building a dictionary with sequential key values
list1 = ["house","sea","sea","sea","montain","house","montain"]
e = enumerate(list1)
#The enumerate() function adds a counter to an iterable (such as a list), returning a sequence of (index, element) pairs or tuples.
print("Enumerate(list1) result: ",enumerate(list1))
for element in e:
    print(element)
dictionary = dict(enumerate(list1))
#Transforms tuples into dictionary elements with a key and a value
print("Dictionary will be: ",dictionary)


#building a dictionary as combination of two sequences keys-value
keys = "abcdefg"
values_list = ["house","sea","sea","sea","montain","house","montain"]

dictionary = dict(zip(keys,values_list))
#Creates a sequence of pairs (tuples) formed by the first element of keys with the first of values_list
# and convert these pairs into a dictionary
print("Dictionary will be: ",dictionary)
print()


#use a dictionary to simulate a standard deck of poker cards

def main():
    m = cards_create()

    n_cards = int(input("How many cards should I draw? "))
    turn = cards_distribution(m,n_cards)
    print("Turn total value",turn)

def cards_create():
    m = {"Ace of Spades": 1, "Two of Spades": 2, "Three of Spades": 3, "Four of Spades": 4, "Five of Spades": 5, "Six of Spades": 6, "Seven of Spades": 7, "Eight of Spades": 8, "Nine of Spades": 9, "Ten of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10, "Ace of Hearts": 1, "Two of Hearts": 2, "Three of Hearts": 3, "Four of Hearts": 4, "Five of Hearts": 5, "Six of Hearts": 6, "Seven of Hearts": 7, "Eight of Hearts": 8, "Nine of Hearts": 9, "Ten of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10,"Ace of Clubs": 1, "Two of Clubs": 2, "Three of Clubs": 3, "Four of Clubs": 4, "Five of Clubs": 5, "Six of Clubs": 6, "Seven of Clubs": 7, "Eight of Clubs": 8, "Nine of Clubs": 9, "Ten of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10,"Ace of Diamonds": 1, "Two of Diamonds": 2, "Three of Diamonds": 3, "Four of Diamonds": 4, "Five of Diamonds": 5, "Six of Diamonds": 6, "Seven of Diamonds": 7, "Eight of Diamonds": 8, "Nine of Diamonds": 9, "Ten of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10}
    return(m)

def cards_distribution(m,n_cards):
    turn = 0
    if n_cards > len(m):
        n_cards = len(m)
    for c in range(n_cards):
        card,value = m.popitem()
        print(card)
        turn += value
    return turn


main()