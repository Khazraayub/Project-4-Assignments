import random

# Word bank with clues
word_bank = {
    "astronomy": "🌌 The study of stars, planets, and the universe.",
    "algorithm": "🧮 A step-by-step procedure to solve a problem.",
    "volcano": "🌋 A mountain that can erupt with lava.",
    "microscope": "🔬 A tool used to see tiny objects.",
    "ballet": "🩰 A graceful style of dance with strict technique."
}

# Function to show the emoji-based hangman status
def show_status(tries_left):
    emojis = {
        6: "🟢 You're just getting started!",
        5: "🟡 Nice moves!",
        4: "🟠 Keep going!",
        3: "🔴 Getting risky...",
        2: "⚠️ Danger zone!",
        1: "🚨 Last shot!",
        0: "💣 Boom! Out of tries!"
    }
    print("Status:", emojis[tries_left])

# Pick a random word and hint
target_word, clue = random.choice(list(word_bank.items()))
hidden_word = ["_" for _ in target_word]
guessed_letters = []
lives = 6

# Game begins
print("🎯 Welcome to the Python Hangman Showdown!")
print(f"🧠 Clue: {clue}")
print("Your word: " + " ".join(hidden_word))
show_status(lives)
print()

# Loop until word guessed or lives exhausted
while lives > 0 and "_" in hidden_word:
    guess = input("🔤 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single alphabet character.\n")
        continue

    if guess in guessed_letters:
        print(f"⛔ You've already guessed '{guess}'. Try another letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in target_word:
        print(f"✅ Yes! '{guess}' is correct!\n")
        for i, char in enumerate(target_word):
            if char == guess:
                hidden_word[i] = guess
    else:
        lives -= 1
        print(f"❌ Nope! '{guess}' isn’t in the word. Lives left: {lives}\n")

    print("Word: " + " ".join(hidden_word))
    show_status(lives)
    print("📜 Guessed so far:", ", ".join(guessed_letters), "\n")

# Final result
if "_" not in hidden_word:
    print(f"🎉 You nailed it! The word was '{target_word}'!")
else:
    print(f"💀 Game over. The word was '{target_word}'. Better luck next time!")
