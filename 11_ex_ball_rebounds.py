# Ball Bounces

print("BALL BOUNCES")
h = 0.0  # height
i = 0  # bounces
while h <= 1:
    h = float(input("Enter the height from which the ball is dropped in cm (h>1): "))
while h > 1:  # when the height becomes less than 1, the loop stops
    h *= 0.8  # multiply height by the reduction percentage (80%) after each bounce
    i = i + 1  # count the number of bounces until the height is less than 1 cm
    print("Bounce no.", i, "Height in cm: ", h)
print("The number of bounces is: ", i)
print("The final height is: ", h, "cm")