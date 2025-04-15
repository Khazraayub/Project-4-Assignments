# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time



def get_first_element(lst):
    # Print the first element of the list
    print("The first element is:", lst[0])

def main():
    num_elements = int(input("How many elements do you want to enter? "))
    user_list = []

    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    
    get_first_element(user_list)

if __name__ == '__main__':
    main()
