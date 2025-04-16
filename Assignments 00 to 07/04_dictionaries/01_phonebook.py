# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.



def main():
    phonebook = {}  # Dictionary to store name -> phone number pairs

    while True:
        name = input("Enter a name (or press enter to finish): ")
        if name == "":
            break
        number = input(f"Enter a phone number for {name}: ")
        phonebook[name] = number

    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

if __name__ == '__main__':
    main()
