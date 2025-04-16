# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.


# Add 'mango' at the end of the list. 


# Print the updated list.



def main():
    # Create a list called fruit_list with the specified fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("\nThe length of the fruit list is:", len(fruit_list))
    print("\nThe fruit list is:",(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("\nThe updated length of the fruit list is:", len(fruit_list))
    print("\nThe updated fruit list is:", fruit_list)

# Run the main function
if __name__ == "__main__":
    main()







# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.





def access_element(lst, index):
    """
    Function to access the element at the given index.
    If the index is out of range, return an appropriate message.
    """
    if index < 0 or index >= len(lst):
        return "Index out of range."
    else:
        return lst[index]

def modify_element(lst, index, new_value):
    """
    Function to modify the element at the given index.
    If the index is out of range, return an appropriate message.
    """
    if index < 0 or index >= len(lst):
        return "Index out of range."
    else:
        lst[index] = new_value
        return f"Element at index {index} has been updated to {new_value}."

def slice_list(lst, start, end):
    """
    Function to slice the list from start index to end index.
    If indices are out of range, handle the error and return an appropriate message.
    """
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice indices."
    else:
        return lst[start:end]

def main():
    # Initialize a list with at least 5 different elements
    elements = [10, 'apple', 3.14, 'banana', 42]
    
    while True:
        print("\nWelcome to the Index Game!")
        print("Please choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter the operation number (1-4): ")

        if choice == '1':
            index = int(input("Enter the index of the element you want to access: "))
            print(access_element(elements, index))

        elif choice == '2':
            index = int(input("Enter the index of the element you want to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(elements, index, new_value))

        elif choice == '3':
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            print(slice_list(elements, start, end))

        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid operation.")

# Run the main function to start the game
if __name__ == "__main__":
    main()
