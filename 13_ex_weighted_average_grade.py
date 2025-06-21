# Weighted Grade Average

print("WEIGHTED GRADE AVERAGE")

sum_grade = 0
sum_credits = 0

grade = int(input("Enter grade: "))

if grade >= 18:
    while grade >= 18 and grade <= 30:
        credits = -1
        while credits <= 0:
            credits = int(input("Enter credits (CFU): "))
        sum_grade += grade * credits
        sum_credits += credits
        grade = int(input("Enter grade: "))
        
        #print("The sum of the grades + credits is: ", sum_grade)
        #print("The sum of the credits is: ", sum_credits)
    print("The weighted grade average is: ", float(sum_grade / sum_credits))
else:
    print("Invalid grade")