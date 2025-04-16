# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.




import random

def play_round():
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"\nYour number is: {your_number}")
    guess = input("Do you think your number is (H)igher or (L)ower than the computer's number? ").strip().upper()

    if guess not in ['H', 'L']:
        print("Invalid input. Please enter H or L.")
        return 0

    print(f"The computer's number was: {computer_number}")
    
    if (guess == 'H' and your_number > computer_number) or (guess == 'L' and your_number < computer_number):
        print("You guessed right! You get a point.")
        return 1
    else:
        print("Oops! Wrong guess. No point this time.")
        return 0

def main():
    print("🎮 Welcome to the High-Low Game! 🎮")
    print("Try to guess if your number is higher or lower than the computer's number.\n")
    
    rounds = int(input("How many rounds would you like to play? "))
    score = 0
    
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        score += play_round()

    print(f"\nGame over! You scored {score} out of {rounds}.")

if __name__ == "__main__":
    main()
