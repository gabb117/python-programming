#Target_matrix.py

def view_matrix(m):
    rows = len(m)
    columns = len(m[0])
    for i in range(rows):
        for j in range(columns):
            print(m[i][j], end = "\t")
        print("")


def load_target_matrix(n):
    m = [0] * n
    for i in range(n):
        row = [0] * n
        m[i] = row

    b = [False] * n
    for i in range(n):
        row = [False] * n
        b[i] = row

    i = n // 2
    j = n // 2
    m[i][j] = 1
    b[i][j] = True

    k = 2
    while n // 2 - k + 1 >= 0:
        for i in range(n // 2 - k + 1, n // 2 + k):
            for j in range(n // 2 - k + 1, n // 2 + k):
                if not (b[i][j]):
                    m[i][j] = k
                    b[i][j] = True
        k += 1
        view_matrix(b)
        print("")

    return(m)


def main():
    n = 0
    while n % 2 == 0:
        n = int(input("Enter number of rows//columns of square matrix: "))
        m = load_target_matrix(n)
        view_matrix(m)

main()
