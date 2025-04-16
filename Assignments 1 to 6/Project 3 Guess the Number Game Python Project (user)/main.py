def user_thinks_computer_guesses():
    print("🤖 Welcome to the Reverse Guess the Number Game!")
    print("Think of a number between 1 and 100, and I (the computer) will try to guess it.")
    print("You'll tell me if I'm too high, too low, or correct.")
    print("I have only 7 chances to guess it!\n")

    low = 1
    high = 100
    chances = 7
    attempts = 0

    while attempts < chances and low <= high:
        guess = (low + high) // 2
        print(f"Attempt {attempts + 1} of {chances}: Is your number {guess}?")
        user_feedback = input("Enter 'high' if too high, 'low' if too low, or 'correct' if I got it: ").lower()

        if user_feedback == 'correct':
            print(f"🎉 Yay! I guessed it in {attempts + 1} tries! Your number was {guess}.")
            break
        elif user_feedback == 'high':
            high = guess - 1
        elif user_feedback == 'low':
            low = guess + 1
        else:
            print("❌ Invalid input! Please type 'high', 'low', or 'correct'.")
            continue

        attempts += 1
    else:
        print("\n😥 I couldn’t guess your number within the limit. You win this time!")

# Run the game
user_thinks_computer_guesses()
