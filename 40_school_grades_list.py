#school grade

def read_grades(infile):
    grades = list() #create a new list to insert grades

    for line in infile: #Iterates through each line of the open file (infile).
        grades.append(int(line.rstrip('\n')))
        #Each line is read as a string and assigned to the line variable.
        #Removes the newline character (\n) at the end of each line.
        #Converts the string (without newlines) to an integer.
        #If the string is not convertible to a number, this will generate an error (ValueError).
        #With grades.append(...) adds the converted number to the grades list.
    return grades


def total_calculation(grades):
    # Initialize the accumulator variable to store the sum of elements
    acc = 0
    
    # Iterate through each element in the grades list
    for elem in grades:
        # Add the current element to the accumulator
        acc += elem
    
    # Return the total sum of all elements
    return acc


def main():
    infile = open('school_grades.txt','r')#read mode on file text 
    grades = read_grades(infile) #read the result of function 'read_grades'

    tot = total_calculation(grades) #read the result of function 'total_calculation'
    average = float(tot) / len(grades) 
    #returns the average between the result of function total_calculation and the length of read_grades function 
    print("Average is: ",format(average,'.2f'))

main()

