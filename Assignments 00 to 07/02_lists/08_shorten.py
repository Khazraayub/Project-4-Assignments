# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


MAX_LENGTH: int = 3  # Define the maximum length for the list

def shorten(lst):
    """
    Removes elements from the end of the list until it is no longer than MAX_LENGTH,
    printing each removed element.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element from the list
        print(f"Removed: {last_elem}")  # Print the removed element

# No need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    The loop stops when the user presses enter without typing anything.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)  # Add the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Prompt for next element
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    print("Original list:", lst)
    shorten(lst)  # Call the shorten function to modify the list
    print("Modified list:", lst)  # Print the modified list

if __name__ == '__main__':
    main()
