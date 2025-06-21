#ordinal of a date

def d_month(m):
    days_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_month[m-1]

def leap_year(year):
    return(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def main():
    d = int(input("Day: "))
    m = int(input("Month: "))
    y = int(input("Year: "))

    if m == 1:
        print("Ordinal of date ",d,"/",m,"/",y," is: ",d,sep = "")

    else:
        ordinal = 0
        for i in range(1,m):
            ordinal += d_month(i) 
            
        ordinal += d
        if leap_year(y) and m > 2:
            ordinal += 1
        print("Ordinal of date ",d,"/",m,"/",y," is: ",ordinal,sep = "")


main()