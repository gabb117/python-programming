# CALCULATING NEW TIME

i = 0          # Variable to count how many days have passed (every 24 hours)
h = -1         # Initialize h to -1 to enter the while loop

# Controlled input for hours (only accepts values between 0 and 23)
while h < 0 or h > 23:
    h = int(input("Enter the hour: "))

m = -1         # Initialize m to -1 to enter the while loop

# Controlled input for minutes (only accepts values between 0 and 59)
while m < 0 or m > 59:
    m = int(input("Enter the minute: "))

s = -1         # Initialize s to -1 to enter the while loop

# Controlled input for seconds (only accepts values between 0 and 59)
while s < 0 or s > 59:
    s = int(input("Enter the second: "))

# Ask how many seconds to add to the time
s2 = int(input("Enter the number of seconds to add: "))

# Print the initial time in hh:mm:ss format
print("Initial time: ", f"{h}:{m}:{s}")

# Convert the seconds to add into hours, minutes, and seconds
h_diff = s2 // 3600        # whole hours to add
m_diff = (s2 // 60) % 60   # remaining minutes to add
s_diff = s2 % 60           # remaining seconds to add

# (Optional: print the calculated values for checking)
print(h_diff)
print(m_diff)
print(s_diff)

# Add the seconds and calculate any minutes to carry over
s += s_diff
m_diff += s // 60          # if seconds exceed 59, add 1 minute
s = s % 60                 # keep only the remaining seconds

# Add the minutes and calculate any hours to carry over
m += m_diff
h_diff += m // 60          # if minutes exceed 59, add 1 hour
m = m % 60                 # keep only the remaining minutes

# Add the calculated hours
h += h_diff

# If the hours exceed 23, calculate how many days have passed
if h > 23:
    i = h // 24            # how many times 24 hours have been exceeded
    h = h % 24             # keep only the remaining hours

# If one or more days have passed, prepare a string to add to the output
if i > 0:
    day = "day +" + str(i)
else:
    day = ""

# Print the final time, with the possible "day +" addition
print("Final time: ", f"{h}:{m}:{s} ", day)