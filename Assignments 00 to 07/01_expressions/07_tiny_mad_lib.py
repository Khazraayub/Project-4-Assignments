# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!


def main():
    # Ask user for positive coding-related inputs
    language = input("Enter a coding language: ")
    achievement = input("Enter a coding achievement: ")
    hours = input("Enter a number of hours: ")

    # Combine inputs into a positive and motivational sentence
    print(f"After {hours} hours of coding in {language}, I built my {achievement} project and I'm so proud of my progress!")

# Run the program
if __name__ == "__main__":
    main()
