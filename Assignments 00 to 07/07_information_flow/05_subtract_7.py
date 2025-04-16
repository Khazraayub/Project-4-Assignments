# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.



# Helper function to subtract 7 from num
def subtract_seven(num):
    return num - 7

# Main function to prompt the user and call the helper function
def main():
    # Prompt the user for a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and print the result
    result = subtract_seven(num)
    print(f"Result after subtracting 7: {result}")

# Run the main function
if __name__ == "__main__":
    main()
