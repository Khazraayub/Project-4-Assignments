# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


def main():
    # Ask the user to enter a length in feet
    feet = float(input("Enter length in feet: "))

    # Convert to inches (1 foot = 12 inches)
    inches = feet * 12

    # Display the result
    print(f"{feet} feet is {inches} inches.")

# Run the program
if __name__ == "__main__":
    main()
