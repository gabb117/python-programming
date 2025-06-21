#days in a month with list
#February with 28 days by default

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

m = int(input("Enter number of month: "))

print("Month: ",month[m-1],'\n',"Days: ",days_in_month[m-1])

