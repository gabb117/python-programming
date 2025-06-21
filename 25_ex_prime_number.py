#prime number

def prime(n):
    div = 2
    while div < n:
        if n % div == 0:
            print(div)
            return False
        div += 1
        print(div)
    return True


def main():
    num = 0
    while num <= 1:
        num = int(input("Enter a number: "))
    if prime(num):
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

main()
