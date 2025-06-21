#Product of a matrix for a scalar number

import random

def load_matrix():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    m = [0] * r
    for i in range(r):
        rows = [0] * c
        m[i] = rows
    for i in range(r):
        for j in range(c):
            m[i][j] = random.randint(1, 15)
    return m

def view_matrix(m):
    rows = len(m)
    columns = len(m[0])
    for i in range(rows):
        for j in range(columns):
            print(m[i][j], end="\t")
        print("")

def scalar_product(m, x):
    rows = len(m)
    columns = len(m[0])
    for i in range(rows):
        for j in range(columns):
            m[i][j] = m[i][j] * x
    return m

def main():
    m = load_matrix()
    print("Original matrix:")
    view_matrix(m)
    x = int(input("Enter number for scalar product: "))
    m = scalar_product(m, x)
    print("Matrix after scalar product:")
    view_matrix(m)

main()