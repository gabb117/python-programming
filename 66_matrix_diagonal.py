#Calculating the mean of the diagonal of square matrix

# m is a matrix represented as a list of lists or list of rows
def diagonal_mean(m):
    s = 0
    for i in range(len(m)):
        s += m[i][i]
    return s


def matrix_view(m):
    rows = len(m) #Calculate how many rows the matrix m has, len(m) returns the number of rows.
    columns = len(m[0]) #Calculate how many columns the matrix has by measuring the length of the first row.
    for i in range(rows): #Iterates through all rows of the matrix ('i' is the row index).
        for j in range(columns): #For each row i, iterate through all columns (j is the column index).
            print(m[i][j],end = "\t") #Prints the value m[i][j] (i.e. row i, column j) on the same output line.
        print("")


def main():
    m = [[1,4,5,6],[7,8,9,10],[11,12,13,15],[18,19,20,22]] #list of lines. lines = 4
    matrix_view(m)

    print("Mean of the diagonal of square matrix is: ",diagonal_mean(m) / float(len(m)))
   #take the sum of square matrix diagonal and divides for number of elements inside diagonal  


main()