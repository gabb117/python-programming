#distance between two dates

def d_month(m):
    # Restituisce il numero di giorni del mese m (da 1 a 12)
    # Returns the number of days in month m (from 1 to 12)
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_month[m - 1]

def leap_year(year):
    # Verifica se un anno è bisestile
    # Checks if a year is a leap year
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def d_m_diff_calc(gd, gm, gy, ld, lm, ly):
    # Calcola la differenza di giorni tra due date nello stesso anno
    # Calculates the difference in days between two dates in the same year
    sum_gm = 0
    # Somma i giorni tra i mesi intermedi
    # Sum the days between intermediate months
    for i in range(lm + 1, gm):
        sum_gm += d_month(i)
        # Aggiungi un giorno se l'anno è bisestile e il mese è febbraio
        # Add one day if the year is leap and the month is February
        if i == 2 and leap_year(gy):
            sum_gm += 1
    # Aggiungi i giorni del mese finale e sottrai i giorni del mese iniziale
    # Add the days of the final month and subtract the days of the initial month
    sum_gm += gd
    sum_gm += (d_month(lm) - ld)
    return sum_gm

def d_y_diff_calc(gd, gm, gy, ld, lm, ly):
    # Calcola la differenza di giorni tra due date in anni diversi
    # Calculates the difference in days between two dates in different years
    sum_gy = 0
    # Somma i giorni degli anni intermedi
    # Sum the days of intermediate years
    for i in range(ly + 1, gy):
        sum_gy += 365
        # Aggiungi un giorno se l'anno è bisestile
        # Add one day if the year is a leap year
        if leap_year(i):
            sum_gy += 1
    # Somma i giorni rimanenti dell'anno di partenza
    # Sum the remaining days of the starting year
    sum_gy += d_m_diff_calc(31, 12, ly, ld, lm, ly)
    # Somma i giorni trascorsi nell'anno di arrivo
    # Sum the days passed in the destination year
    sum_gy += d_m_diff_calc(gd, gm, gy, 1, 1, gy)
    return sum_gy

def main():
    # Input della prima data (giorno, mese, anno)
    # Input of the first date (day, month, year)
    d1 = int(input("Enter day of first date: "))
    m1 = int(input("Enter month of first date: "))
    y1 = int(input("Enter year of first date: "))

    # Input della seconda data (giorno, mese, anno)
    # Input of the second date (day, month, year)
    d2 = int(input("Enter day of second date: "))
    m2 = int(input("Enter month of second date: "))
    y2 = int(input("Enter year of second date: "))

    # Calcolo delle differenze assolute tra anni, mesi e giorni
    # Calculation of absolute differences between years, months, and days
    y_diff = abs(y1 - y2)
    m_diff = abs(m1 - m2)
    d_diff = abs(d1 - d2)

    # Se gli anni sono uguali
    # If the years are equal
    if y1 == y2:
        # Se i mesi sono uguali, stampa la differenza tra i giorni
        # If the months are equal, print the difference between days
        if m1 == m2:
            print("The difference between the dates is", abs(d1 - d2), "days")
        # Se il mese della prima data è maggiore
        # If the month of the first date is greater
        elif m1 > m2:
            print("The difference between the dates is", d_m_diff_calc(d1, m1, y1, d2, m2, y2), "days")
        # Se il mese della seconda data è maggiore
        # If the month of the second date is greater
        else:
            print("The difference between the dates is", d_m_diff_calc(d2, m2, y2, d1, m1, y1), "days")

    # Se il primo anno è maggiore del secondo
    # If the first year is greater than the second
    elif y1 > y2:
        print("The difference between the dates is", d_y_diff_calc(d1, m1, y1, d2, m2, y2), "days")

    # Se il secondo anno è maggiore del primo
    # If the second year is greater than the first
    else:
        print("The difference between the dates is", d_y_diff_calc(d2, m2, y2, d1, m1, y1), "days")

# Avvio del programma
# Program start
main()