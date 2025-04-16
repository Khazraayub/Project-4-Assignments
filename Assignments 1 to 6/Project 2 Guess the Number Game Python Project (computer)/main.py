import random

def guess_the_number():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is? You have 7 chances to get it right!\n")

    number_to_guess = random.randint(1, 100)
    chances = 7
    attempts = 0

    while attempts < chances:
        try:
            guess = int(input(f"Attempt {attempts + 1} of {chances}: Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 100.\n")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("🚫 Please guess a number within the range 1 to 100.\n")
        elif guess < number_to_guess:
            print("🔻 Too low! Try a higher number.\n")
        elif guess > number_to_guess:
            print("🔺 Too high! Try a lower number.\n")
        else:
            print(f"🎉 Congrats! You guessed the number {number_to_guess} in {attempts} attempts! 🏆")
            break
    else:
        print(f"\n😢 Sorry, you're out of chances. The number was {number_to_guess}. Better luck next time!")

# Run the game
guess_the_number()
