#calculate polygon perimeter

import math  # Imports the math module, used for mathematical operations like square root

# Function to calculate the distance between two points on the Cartesian plane
def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))  
    # Uses the Euclidean distance formula: √[(x2 - x1)^2 + (y2 - y1)^2]

def main():
    perimeter = 0  # Initializes the perimeter to 0
    num_points = 0  # Initializes the number of points

    # Asks the user how many points the polygon has (minimum 2)
    while num_points < 2:
        num_points = int(input("How many points is the polygon composed of? "))
    
    print("Enter the coordinates of the points")

    # Reads the coordinates of the first point
    x_prev = float(input("Enter the x coordinate of point 1: "))
    y_prev = float(input("Enter the y coordinate of point 1: "))

    # Saves the first point to close the polygon later
    x_start = x_prev
    y_start = y_prev

    # Loop to read the remaining points and calculate distance between consecutive ones
    for i in range(2, num_points + 1):
        x_curr = float(input(f"Enter the x coordinate of point {i}: "))
        y_curr = float(input(f"Enter the y coordinate of point {i}: "))
        perimeter += distance(x_prev, y_prev, x_curr, y_curr)  # add distance to the perimeter
        x_prev, y_prev = x_curr, y_curr  # update previous point

    # Close the polygon by adding the distance from the last to the first point
    perimeter += distance(x_prev, y_prev, x_start, y_start)

    
    print(f"The perimeter of the polygon with {num_points} sides is: {perimeter}")


main()