#glob() function
#allows you to locate a file name based on its extension

import glob

print(glob.glob("*.txt"))
print()
#['coffee.txt', 'telephone_book.txt', 'dante.txt', 'temp.txt', 'addresses.txt', 'fairy_tales.txt', 'school_grades.txt']
#it founds all files with .txt extension present in the file

#iglob() function
#same function of glob but it didn't save all the value inside a list, it only show you every file not saving them

import glob

result = glob.iglob("/*")
for a in result:
    print(a)
print()
#show all the file and directory inside pc mass storage

import glob

result = glob.iglob("/dev/*")
for a in result:
    print(a)
print()
#show all file and directory of a specific path

import glob

files = glob.glob("/dev/*.*")
for a in files:    
    print(files)
print()
#it show only files (no folders) of a specifi path

import glob
result = glob.iglob("**/*.txt", recursive=True)
for a in result:
    print(a)
print()
#Searching through files and directories can be a computationally intensive operation, so we resort to using iglob()

#exercise
#combined use of glob() and findall()

import glob
import re

file_list = glob.glob("*.txt")

for text in file_list:
    infile = open(text, 'r')
    result = re.findall(r"art. \d+", infile.read(), re.I)
    for a in result:
        print(a)
    infile.close()
print()
#identify the string type "art." in the .txt files and print it on screen

#Data serialization
#To serialize files you have to convert them into a stream of bytes and retrieve them later. 
#After serialization you can save the sequence to disk
#Text file and binary file have got different encodings, if you try to open a binary file with text editor
#it will be incorrectly interpreted

#Python through "pickle" module contain some functions for serialization, after imported pickle module
#open file in binary mode (write mode), call dump() method to serialize the object anche write him in specific file

import pickle

dictionary = {'X':1, 'Y':2, 'Z':3}

outputfile = open('dictionary.dat','wb')
pickle.dump(dictionary,outputfile)
outputfile.close()
#The code allows you to write a dictionary data structure to a binary file

import pickle
inputfile = open('dictionary.dat','rb')
dictionary = pickle.load(inputfile)
inputfile.close()
print(dictionary)
print()
#Output: {'X': 1, 'Y': 2, 'Z': 3}
#The code allows to read a dictionary data structure from a binary file


#exercise 
#inserting data into a dictionary and saving to a binary file

import pickle

def save_data(file):
    person = dict()
    person["name"] = input("Name: ")
    person["surname"] = input("Surname: ")
    person["city"] = input("City: ")
    pickle.dump(person,file)

def main():
    repeat = 'y'
    outputfile = open("info.dat","wb")#wb = write binary
    #wb" completely overwrites the file every time you run the program,every time you re-run the script, you lose the previous data.
    while repeat.lower() == 'y':
        save_data(outputfile)
        repeat = input("Do you want to enter more data? ")
    outputfile.close()

main()
#This program requires you to enter data and save that data in a dictionary

import pickle

def view_data(p):
    print("Name:",p["name"])
    print("Surname:",p["surname"])
    print("City:",p["city"])
    print()

def main():
    try:
        print("Information about people\n")
        end_of_file = False #It is used to check when the end of the file has been reached.
        infile = open('info.dat','rb')
        while not end_of_file:
        #Until you get to the end of the file, try to read an object (in this case a dictionary) with pickle.load(infile).
            try:
                person = pickle.load(infile)
                view_data(person)
            except EOFError:#If an EOFError exception is raised, it means that the end of the file has been reached.
                end_of_file = True#set end_of_file = True to exit the loop
                infile.close()
    except FileNotFoundError:
        print("Data not available")

main()
#The main problem with the exercise is that a suitable data structure has not been used for the program 
# to load information from a file at startup.

#update
def read_file(filename):
    infile = open(filename,'rb')
    person_list = pickle.load(infile)
    infile.close()
    return person_list

def view_file(person_list):
    for elem in person_list:
        print("Name:",elem["name"])
        print("Surname:",elem["surname"])
        print("City:",elem["city"])
        print()


def save_person(person_list):
    person = dict()
    person["name"] = input("Name: ")
    person["surname"] = input("Surname: ")
    person["city"] = input("City: ")
    person_list.append(person)
    return person_list


def save_file(filename,person_list):
    outputfile = open(filename,'wb')
    pickle.dump(person_list,outputfile)
    outputfile.close()


def main():
    filename = "person.dat"
    person_list = list()
    try:
        print("Information about people\n")
        person_list = read_file(filename)
    except FileNotFoundError:
        print("Data not available")

    print("Adding new people")
    repeat = 'y'
    while repeat.lower() == 'y':
        save_person(person_list)
        repeat = input("Do you want to enter more data? ")
    save_file(filename, person_list)

main()
#added change, now the program saves all updated data back to the file


