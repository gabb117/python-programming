#Spinner of numbers

def view_matrix(m):
    rows = len(m)
    columns = len(m[0])
    for i in range(rows):
        for j in range(columns):
            print(m[i][j], end = "\t")
        print("")


def load_spin_matrix(n):
    m = [0] * n
    for i in range(n):
        row = [0] * n
        m[i] = row
    
    ic = n // 2
    jc = n // 2
    m[ic][jc] = 1    #central element

    progr = 2
    k = 2

    while n // 2 - k + 1 >= 0:
        for i in range(ic + k - 2, ic - k, -1): #left side towards up
            m[i][jc - k + 1] = progr
            progr += 1

        for j in range(jc - k + 2, jc + k):     #top side to the right
            m[ic - k + 1][j] = progr
            progr += 1

        for i in range(ic - k + 2, ic + k):     #right side towards down
            m[i][jc + k - 1] = progr
            progr += 1

        for j in range(jc + k - 2, jc - k, -1):  #bottom side to the left
            m[ic + k - 1][j] = progr
            progr += 1

        k += 1

    return m 



def main():
    n = 0
    while n % 2 == 0:
        n = int(input("Enter number of rows//columns of square matrix (enter odd number): "))
        m = load_spin_matrix(n)
        view_matrix(m)

main()