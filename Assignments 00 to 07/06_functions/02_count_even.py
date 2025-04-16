# Problem Statement
# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!



def count_even(lst):
    """Counts and prints the number of even numbers in the list."""
    even_count = 0
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
    print(f"There are {even_count} even numbers in the list.")

def get_lst():
    """Prompts the user to enter integers until they press enter without entering anything."""
    lst = []
    while True:
        try:
            user_input = input("Enter an integer or press enter to stop: ")
            if user_input == "":  # Stop if the user presses enter without typing anything
                break
            lst.append(int(user_input))  # Convert input to integer and append to the list
        except ValueError:
            print("That's not a valid integer, please try again.")  # Handle invalid input
    return lst

def main():
    # Populate the list by prompting the user for input
    lst = get_lst()
    # Call count_even to print the number of even numbers
    count_even(lst)

# Run the program
if __name__ == "__main__":
    main()
