# Problem Statement
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):






def main():
    # Set Anton's age
    Anton = 21

    # Beth is 6 years older than Anton
    Beth = Anton + 6

    # Chen is 20 years older than Beth
    Chen = Beth + 20

    # Drew is as old as Chen's age plus Anton's age
    Drew = Chen + Anton

    # Ethan is the same age as Chen
    Ethan = Chen

    # Print names and ages
    print("Anton is", Anton, "years old.")
    print("Beth is", Beth, "years old.")
    print("Chen is", Chen, "years old.")
    print("Drew is", Drew, "years old.")
    print("Ethan is", Ethan, "years old.")

# Run the program
if __name__ == "__main__":
    main()
