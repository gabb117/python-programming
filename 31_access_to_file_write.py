#access to file
#write mode
#logic_file = function(phisycal_file.eg,mode_write_or_read)

def address_write():
    outfile = open('addresses.txt','w')
    #Open a file if already exist, otherwise create the new file
    #In this case 'addresses.txt' is created and by the mode 'w' (write)
    #you can write the file, otherwise for read the file put 'r' (read)

    outfile.write("fifth avenue 156/b\n") 
    #A new string is saved in the file 'addresses.txt' 
    outfile.write("trafalgar square 13\n") 
    #A new string is saved in the file 'addresses.txt'
    outfile.write("abbey road 1/a\n") 
    #A new string is saved in the file 'addresses.txt'

    outfile.close()
    #The access to file is now closed



def favorite_fairy_tales_write():
    print("What are your favorite fairy tales?")
    fairy_tale1 = input("Fairy tale n.1: ")
    fairy_tale2 = input("Fairy tale n.2: ")
    fairy_tale3 = input("Fairy tale n.3: ")
    
    outfile = open('fairy_tales.txt','w')

    outfile.write(fairy_tale1 + '\n')
    outfile.write(fairy_tale2 + '\n')
    outfile.write(fairy_tale3 + '\n')

    outfile.close()
   


def school_grade_write():
    print("Enter three school grades: ")
    g1 = int(input("Grade 1: "))
    g2 = int(input("Grade 2: "))
    g3 = int(input("Grade 3: "))

    outfile = open('school_grades.txt','w')

    outfile.write(str(g1) + '\n')
    outfile.write(str(g2) + '\n')
    outfile.write(str(g3) + '\n')

    outfile.close()



def main():

    address_write()
    favorite_fairy_tales_write()
    school_grade_write()

main()
