# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.


import random

def main():
    # Simulate rolling the first die
    die1 = random.randint(1, 6)
    
    # Simulate rolling the second die
    die2 = random.randint(1, 6)

    # Calculate total
    total = die1 + die2

    # Print results
    print("Die 1 rolled:", die1)
    print("Die 2 rolled:", die2)
    print("Total:", total)

# Run the program
if __name__ == "__main__":
    main()
