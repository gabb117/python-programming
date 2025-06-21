# Import the random library to generate random numbers
import random

# Define constants for the menu options
ROLL = 1      # Option to roll the dice once
SESSION = 2   # Option to perform a dice rolling session
AVERAGE = 3   # Option to calculate the average of rolls
EXIT = 4      # Option to exit the program

# Function to roll a single die
def roll():
    # Generates a random number between 1 and 6 to simulate a die roll
    return random.randint(1,6)

# Function to roll multiple dice a specified number of times
def roll_dice(n_dice, n_rolls):
    acc = 0  # Accumulator for the total number of rolls
    for i in range(n_rolls):  # Loop for the number of rolls
        print("Roll n." + str(i+1))
        for j in range(n_dice):  # Loop for the number of dice
            l = roll()  # Rolls a single die
            print("Die n." + str(j+1) + " = " + str(l))  # Print the result
            acc = acc + 1  # Increase the roll count
        print("")  # Blank line for spacing
    return acc  # Return the total roll count

# Function to perform multiple rolling sessions
def roll_session(n_repetitions, n_dice, n_rolls):
    acc = 0  # Accumulator for total rolls across sessions
    for i in range(n_repetitions):  # Loop through each session
        print("Session n. " + str(i+1))
        acc = acc + roll_dice(n_dice, n_rolls)  # Sum the rolls in each session
        print("\n")  # Blank line for spacing between sessions
    return acc  # Return the total number of rolls

# Calculate the average of the rolls
def rolls_average(total, number):
    # Return the average as a floating-point number
    return float(total) / number

# Print the interactive menu
def show_menu():
    print("\n\tMENU")
    print("1. Roll a dice")
    print("2. Dice roll session")
    print("3. Average of last rolls")
    print("4. Exit")

# Main function to handle the program logic
def main():
    acc = 0  # Accumulator for the number of rolls
    tot_roll_num = 0  # Total number of performed rolls
    choise = 0  # Variable for menu choice

    while choise != EXIT:  # Loop until the user chooses to exit
        show_menu()  # Display the menu
        choise = int(input("Select an option (1-4):\t "))
        print()
        if choise == ROLL:
            num = int(input("Number of dice: "))
            rolls = int(input("Number of rolls per die: "))
            print()
            tot_roll_num = num * rolls
            acc = roll_dice(num, rolls)
        elif choise == SESSION:
            session = int(input("Number of sessions: "))
            num = int(input("Number of dice: "))
            rolls = int(input("Number of rolls per die: "))
            print()
            tot_roll_num = num * rolls * session
            acc = roll_session(session, num, rolls)
        elif choise == AVERAGE:
            print("Average of last rolls: ", format(rolls_average(acc, tot_roll_num), ".2f"))
            print()
        elif choise == EXIT:
            print("Exiting the program, see you!")
        else:
            print("Error, invalid choice!")

main()  #