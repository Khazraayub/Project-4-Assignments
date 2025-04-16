# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high  # Checks if n is between low and high (inclusive)

def main():
    # Ask the user for input values
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    # Call the in_range function and print the result
    result = in_range(n, low, high)
    print(f"Is {n} between {low} and {high}? {result}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
