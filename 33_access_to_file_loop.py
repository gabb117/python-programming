#read/write file with while and for loop

def school_grade_read_while():
    infile = open('school_grades.txt','r')

    line = infile.readline()

    while line != '':
        print(line,end='')
        line = infile.readline()

    infile.close()

def school_grade_read_for():
    infile = open('school_grades.txt','r')

    line = infile.readline()

    for line in infile:
        print(line, end='')
    

    infile.close()


def main():
    school_grade_read_while()
    school_grade_read_for()

main()