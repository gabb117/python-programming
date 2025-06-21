#Matrix product

import random

def load_matrix(r1,c,c2):
    c1 = c 
    r2 = c 
    a = [0] * r1
    for i in range(r1):
        row = [0] * c1
        a[i] = row
    for i in range(r1):
        for j in range(c1):
            a[i][j] = random.randint(1,15)

    b = [0] * r2
    for i in range(r2):
        row = [0] * c2
        b[i] = row
    for i in range(r2):
        for j in range(c2):
            b[i][j] = random.randint(1,15)

    return a,b 


def view_matrix(m):
    rows = len(m)
    columns = len(m[0])
    for i in range(rows):
        for j in range(columns):
            print(m[i][j], end = "\t")
        print("")


def matrix_product(a,b):
    r1 = len(a)
    c1 = len(a[0])
    r2 = len(b)
    c2 = len(b[0])

    c = [0] * r1
    for i in range(r1):
        row = [0] * c2
        c[i] = row 

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                c[i][j] += a[i][k] * b[k][j]
    return c 

def main():
    r1 = int(input("Enter number of rows of matrix A: "))
    c = int(input("Enter number of columns of matrix A = rows of matrix B: "))
    c2 = int(input("Enter number of columns of matrix B: "))
    a,b = load_matrix(r1,c,c2)

    print("\nMatrix A")
    view_matrix(a)
    print("\nMatrix B")
    view_matrix(b)
    result = matrix_product(a,b)
    print("\nMatrix C=AB")
    view_matrix(result)

main()