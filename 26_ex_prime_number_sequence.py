def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter a number > 3: "))
    
    print("Prime numbers: ", n, ":")
    print("1")
    print("2")
    for num in range(3, n + 1):  # parte da 3 e arriva fino a n incluso
        if is_prime(num):
           
            print(num)
    
main()