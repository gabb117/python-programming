#calculation of the distance on the cartesian plane

import math

def distance(x1,y1,x2,y2):
    return (math.sqrt(pow(x1-x2,2)+ pow(y1-y2,2)))

def main():
    x1=int(input("Enter x1: "))
    y1=int(input("Enter y1: "))
    x2=int(input("Enter x2: "))
    y2=int(input("Enter y2: "))
    print("The distance between the two point is: ",distance(x1,y1,x2,y2))

main()