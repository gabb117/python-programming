#tax code manipulation
#a string of 16 characters

import mysql.connector

vowels = "aeiouAEIOU"  #Creates a string with all vowels, both lowercase and uppercase.

months = {'01' : 'A','02' : 'B','03' : 'C','04' : 'D','05' : 'E','06' : 'H','07' : 'L','08' : 'M','09' : 'P','10' : 'R','11' : 'S','12' : 'T',}
#dictionary, associate the month number with a letter

even = {'0':1,'1':0,'2':5,'3':7,'4':9,'5':13,'6':15,'7':17,'8':19,'9':21,'A':1,'B':0,'C':5,'D':7,'E':9,'F':13,'G':15,'H':17,'I':19,'J':21,'K':2,'L':4,'M':18,'N':20,'O':11,'P':3,'Q':6,'R':8,'S':12,'T':14,'U':16,'V':10,'W':22,'X':25,'Y':24,'Z':23}

odd = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

controll = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}




def surname_calc(surname):
    #Create two empty lists:
    cons = [] #cons: to collect consonants
    vow = []  #vow: to collect vowels

    for x in surname:  #Scroll through each letter x of the last name
        if x in vowels: 
            vow.append(x)  #If it is a vowel, it puts it in vow
        else:
            cons.append(x)  #If it is a consonant, it puts it in cons
    
    codeSurname = "".join(cons + vow + ['x'] * 2) [0:3]
    #Combine three lists: list of consonants, list of vowels and a list of two characters 'x' and the take the first three letter by [0:3]
    #all elements of lists joined in a single string 
    return codeSurname.upper() 


def name_calc(name):
    cons = [] #cons: to collect consonants
    vow = []  #vow: to collect vowels

    for x in name:  #Scroll through each letter x of the last name
        if x in vowels: 
            vow.append(x)  #If it is a vowel, it puts it in vow
        else:
            cons.append(x)  #If it is a consonant, it puts it in cons

    if len(cons) > 3:
        cons[1:2] = []
        #This syntax removes the element at index 1 from the cons list
        #The slice cons[1:2] contains the element at index 1 (the second element). 
        #Assigning [ ] to it means removing the element at index 1.

    codeName = "".join(cons + vow + ['x'] * 2) [0:3]
    #Combine three lists: list of consonants, list of vowels and a list of two characters 'x' and the take the first three letter by [0:3]
    #all elements of lists joined in a single string 
    return codeName.upper()  


def adj_date(date,gender):
    year = date[2] [2:] #Takes the last 2 digits of the year from the index[2] of date
    month = months[date[1]]#Get the month code (using the dictionary)
    if gender.upper() != "M":
        day = str(int(date[0]) + 40)#If the gender is female, it adds 40 to the day
    else:
        day = date[0]#Use the day as it is (male)
    
    return year + month + day


def cad_id(municip):
    codes = open("cadastral_codes.csv","r")
    for line in codes:
        municips = line.split(',')
        if municips[0].upper().strip() == municip.upper():
            codes.close()
            return municips[1].upper().rstrip()
    codes.close()
    return "WRONG MUNICIP"


def controll_code(taxCode):
    index = 0
    a = 0
    b = 0
    p = list()
    d = list()
    while index < len(taxCode):
        if index % 2 != 0:
            d.append(taxCode[index])
        else:
            p.append(taxCode[index])
        index += 1
    
    for x in d:
        a += odd[x.upper()]
    for y in p:
        b += even[y.upper()]
    return controll [((a+b)%26)].upper()

def save_tax_code(tax_code): #save all tax codes inside a database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="gabriele",
        password="unipegaso",
        db="tax_codes"
    )
    
    cursor = conn.cursor()

    query = "INSERT INTO tax_codes (code) VALUES (%s)"
    cursor.execute(query, (tax_code,))

    conn.commit()
    print("Tax code saved:", tax_code)

    cursor.close()
    conn.close()

def main():
    surname1 = input("Enter surname: ")
    surname = surname1.replace(" ","")
    name1 = input("Enter name: ")
    name = name1.replace(" ","")
    gender = input("Enter the gender (F or M): ")
    while len(gender) != 1:
        gender = input("Enter the gender (F or M): ")
    date = input("Enter birthdate (DD/MM/YYYY): ").split('/')
    municip = input("Enter city of birth: ")

    tax_code = surname_calc(surname)+name_calc(name)+adj_date(date,gender)+cad_id(municip)
    print(tax_code + controll_code(tax_code))
    save_tax_code(tax_code + controll_code(tax_code))

main()




