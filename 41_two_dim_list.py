#two dimensional list

LINES = 3
COLUMNS = 4

def main():
    values = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    a = 0

    for i in range(LINES):
        for j in range(COLUMNS):
            values[i][j] = a
            a += 1
    print(values) # default view [0,1,2,3],[4,5,6,7],[8,9,10,11]

    for i in range(LINES):
        print(values[i])
        #correct view of a two-dimensional list
        # [0,1,2,3]
        # [4,5,6,7]
        # [8,9,10,11]

main()