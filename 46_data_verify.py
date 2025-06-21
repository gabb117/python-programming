#data verify

def d_month(n):
    d_month = [31,29,31,30,31,31,30,31,30,31]
    return (d_month[n-1])

def leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def d_m_error(d,m):
    if d <= d_month(m):
        return False
    else:
        return True

def date_error(d,m,y):
    if not(leap_year(y)) and m == 2:
        if d == 29:
            return True
        else:
            return False


def main():
    d = 40
    m = 40
    y = -10
    date_ok = False
    print("Enter a date between 01/01/1990 and 31/12/2030")

    
    while date_ok == False:
        while d <= 0 or d > 31:
            d = int(input("Day: "))
        while m <= 0 or m > 12:
            m = int(input("Month: "))
        while y < 1990 or y > 2030:
            y = int(input("Year: "))
    
        if d_m_error(d,m) or date_error(d,m,y):
            print("Date entered is not in range")
            d = 40
            m = 40
            y = -10
        else:
            date_ok = True
            print("Valid date")

main()