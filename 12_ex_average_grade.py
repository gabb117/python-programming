# Grade Average

print("GRADE AVERAGE")

sum_grades = 0
count = 0
grade = int(input("Enter grade: "))
if grade >= 18:
    while grade >= 18 and grade <= 30:  # enter grades from 18 to 30 inclusive
        sum_grades += grade  # sum each entered grade
        count = count + 1  # count the number of grades for division after input
        grade = int(input("Enter grade: "))  # repeat the grade entry until the condition is no longer met
    print("The sum of the grades is: ", sum_grades)
    print("The average of the grades is: ", float(sum_grades) / count)
else:
    print("Invalid grade")