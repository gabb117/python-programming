def d_month(n):
    d_month = [31,29,31,30,31,31,30,31,30,31]
    return (d_month[n-1])

def leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def d_m_error(d,m):
    if d <= d_month(m):
        return False #there is not an error
    else:
        return True #there is an error

def date_error(d,m,y):
    if not(leap_year(y)) and m == 2:
        if d == 29:
            return True #there is an error - not leap year
        else:
            return False #there is not an error - leap year

def insert_data ():
    d = 40
    m = 40
    y = -10
    date_ok = False
    print("Enter a date between 01/01/1990 and 31/12/2030")
    while date_ok == False:
        while d <= 0 or d > 31:
            d = int(input("Day: "))
        while m <= 0 or m >12:
            m = int(input("Month: "))
        while y < 1990 or y > 2030:
            y = int(input("Year: "))
        if not(d_m_error(d,m) or date_error(d,m,y)):
            return d,m,y


def ord_date(d,m,y):
    if m == 1:
        return d
    else:
        ordinal = 0
        for i in range(1,m):
            ordinal += d_month(i)
        ordinal += d
        if leap_year(y) and m > 2:
            ordinal += 1
        return ordinal


def end_date(d,m,y):
    if m == 12:
        return d_month(12) - d
    else:
        missing = 0
        for i in range(12,m,-1):
            missing += d_month(i)
        missing += d_month(m) - d
        if leap_year(y) and m <= 2:
            missing += 1
        return missing


def d_m_diff_calc(gd, gm, gy, ld, lm, ly):
    
    # Calculates the difference in days between two dates in the same year
    sum_gm = 0
    
    # Sum the days between intermediate months
    for i in range(lm + 1, gm):
        sum_gm += d_month(i)
       
        # Add one day if the year is leap and the month is February
        if i == 2 and leap_year(gy):
            sum_gm += 1
    
    # Add the days of the final month and subtract the days of the initial month
    sum_gm += gd
    sum_gm += (d_month(lm) - ld)
    return sum_gm

def d_y_diff_calc(gd, gm, gy, ld, lm, ly):
    
    # Calculates the difference in days between two dates in different years
    sum_gy = 0
 
    # Sum the days of intermediate years
    for i in range(ly + 1, gy):
        sum_gy += 365
       
        # Add one day if the year is a leap year
        if leap_year(i):
            sum_gy += 1

    # Sum the remaining days of the starting year
    sum_gy += d_m_diff_calc(31, 12, ly, ld, lm, ly)
    
    # Sum the days passed in the destination year
    sum_gy += d_m_diff_calc(gd, gm, gy, 1, 1, gy)
    return sum_gy



def diff_date(d1,m1,y1,d2,m2,y2):
    if y1 == y2:
        if m1 == m2:
            return abs(d1 - d2)
        elif m1 > m2:
            return  d_m_diff_calc(d1,m1,y1,d2,m2,y2)
        else:
             d_m_diff_calc(d2,m2,y2,d1,m1,y1)
    elif y1 > y2:
        return d_y_diff_calc(d1,m1,y1,d2,m2,y2)
    else:
        return d_y_diff_calc(d2,m2,y2,d1,m1,y1)


def month_increase(m,y):
    if m == 12:
        y += 1
        m = 1
    else:
        m += 1
    return m,y


def date_sum(d,m,y,dd):
    diff = d_month(m) - d #how much is left until the end of the month of that year and subsequent correction if it is a leap year
    if m == 2 and leap_year(y):
        diff += 1
    if dd <= diff:
        return d + dd,m,y 
    else:                    #if it goes to the first day of the following month
        dd -= diff           #if the month is December the year starts
        d = 1
        m,y = month_increase(m,y)

        print("Month: ",m,"\tYear: ",y,"\tDD = ",dd)

        while dd > 31:       #to "consume" months with years advancement until a number of days less than 31 is reached
            dd -= d_month(m)
            if m == 2 and leap_year(y):
                dd -= 1
            m,y = month_increase(m,y)
            print("Month: ",m,"\tYear: ",y,"\tDD = ",dd)

        if d > d_month(m):
            dd -= d_month(m)
            m,y = month_increase(m,y)

        d = dd
        return d,m,y 


def month_decrease(m,y):
    if m == 1:
        y -= 1
        m = 12
    else:
        m -= 1

    return m,y


def decrease_date(d,m,y,dd):
    if dd < d:
        return d - d,m,y
    else:                     #move on to the last day of the previous month
        dd -= d               #if the month is January, the year starts
        m,y = month_decrease(m,y)
        d = d_month(m)
        print("Month: ",m,"\tYear: ",y,"\tDD = ",dd)

        while dd > 30:
            dd -= d_month(m)
            if m == 2 and leap_year(y):
                dd -= 1
            m,y = month_decrease(m,y)
            d = d_month(m)
            print("Month: ",m,"\tYear: ",y,"\tDD = ",dd)

        if dd > d_month(m):
            dd -= d_month(m)
            m,y = month_decrease(m,y)

        d = d_month(m) - dd
        return d,m,y

    
def main():

    i = 0
    while i != 6:
        print("\t\tMENU")
        print("1. Number of days passed since the beginning of the year")
        print("2. Number of days left until the end of the year")
        print("3. Distance between two dates")
        print("4. Add days to a date")
        print("5. Subtract days from a date")
        print("6. Quit")

        i = int(input("\nEnter your choice: "))

        if i == 1:
            d,m,y = insert_data()
            print("The number of days passed since 01/01/",y," is equal to ",ord_date(d,m,y)," days",sep="")

        elif i == 2:
            d,m,y = insert_data()
            print("The number of days remaining until 31/12/",y," is equal to ",end_date(d,m,y)," days",sep="")

        elif i == 3:
            print("FIRST DATE")
            d,m,y = insert_data()
            print("SECOND DATE")
            d1,m1,y1 = insert_data()
            print("The distance between ",d,"/",m,"/",y," and ",d1,"/",m1,"/",y1," is equal to ",diff_date(d,m,y,d1,m1,y1)," days",sep="")

        elif i == 4:
            d,m,y = insert_data()
            dd = int(input("Enter the number of days to add to the date: "))
            d1,m1,y1 = date_sum(d,m,y,dd)
            print("New date is ",d1,"/",m1,"/",y1,sep="")

        elif i == 5:
            d,m,y = insert_data()
            dd = int(input("Enter the number of days to subtract to the date: "))
            d1,m1,y1 = decrease_date(d,m,y,dd)
            print("New date is ",d1,"/",m1,"/",y1,sep="")

        elif i == 6:
            print("I'm leaving the program...")

        else:
            print("Invalid choise")
        print("")



main()
            