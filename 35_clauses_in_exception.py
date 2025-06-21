#exception checking, using "excep...as", "else" and "finally"

def main():
    try:
        infile = open('school_grades.txt','r')

        total = 0
        counter = 0

        for line in infile:
            grade = int(line.rstrip('\n'))
            total = total + grade
            counter = counter + 1
            average = float(total)/counter

    except Exception as error:
        print(error)

    else:
        print("The average of grades is: ",format(average),'.2f')

    finally:
        infile.close()

main()