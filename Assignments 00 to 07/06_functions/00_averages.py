# Problem Statement
# Write a function that takes two numbers and finds the average between the two.


def find_average(num1, num2):
    # Calculate the average of the two numbers
    average = (num1 + num2) / 2
    return average

def main():
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Find the average using the function
    avg = find_average(num1, num2)
    
    # Print the result
    print(f"The average of {num1} and {num2} is: {avg}")

# Run the main function
if __name__ == "__main__":
    main()
