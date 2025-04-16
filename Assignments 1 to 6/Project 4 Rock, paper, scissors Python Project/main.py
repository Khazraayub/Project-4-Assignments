import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock 🪨, Paper 📄, Scissors! ✂️")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("Type 'rock', 'paper', or 'scissors' to make your move.\n")

    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        print(f"\n🔁 Round {round_num} of {rounds}")
        user_choice = input("Your move: ").lower()
        if user_choice not in choices:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("⚖️ It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("✅ You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

    print("\n🎉 Game Over!")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print("🏆 You are the overall winner!")
    elif user_score < computer_score:
        print("🤖 The computer wins the game!")
    else:
        print("🤝 It's a draw!")

# Start the game
rock_paper_scissors()
