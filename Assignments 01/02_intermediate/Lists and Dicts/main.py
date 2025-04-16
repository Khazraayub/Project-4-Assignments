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
