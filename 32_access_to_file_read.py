#access  to file
#read mode

def address_read():
    infile = open('addresses.txt','r')
    #open the file in read mode
    
    content = infile.read()
    #copy the file in a variable with function read()
    
    infile.close()
    #close the first file,leaving the content open to be read

    print(content)
    #print the contet of variable with the addresses.txt file
    #if don't know how many line saved inside the file,it will print 
    #everything is inside 





#if know what is inside the file ,so we can choose what to print
def address_read_2():
    infile = open('addresses.txt','r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    #it reads each three line in text file and copy in every variable

    infile.close()
    #close the file

    print(line1, end = '')
    print(line2, end = '')
    print(line3, end = '')
    #print the text saved in every line of the file,also with the 
    #backspace '\n' (removed by end = '').



#rstrip() to remove the \n new line of the input read mode
def favorite_fairy_tales_read():
    infile = open('fairy_tales.txt','r')
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    #"rstrip" delete every character o space leaved at the right
    #of every string inside the text

    infile.close()

    print(line1)
    print(line2)
    print(line3)



def school_grade_read():
    infile = open('school_grades.txt','r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    infile.close()
    
    g1 = int(line1) 
    g2 = int(line2)
    g3 = int(line3)
    #before print the grades written in text file, they need to be 
    #converted to integer
    print(line1,line2,line3)



def main():
    address_read()
    address_read_2()
    favorite_fairy_tales_read()
    school_grade_read()

main()


