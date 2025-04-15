# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.



import random

def roll_dice():
    # Local variables inside the function
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1:", die1, "Die 2:", die2)

def main():
    print("Rolling two dice three times...\n")

    # Call roll_dice three times
    roll_dice()
    roll_dice()
    roll_dice()

# Run the program
if __name__ == "__main__":
    main()
