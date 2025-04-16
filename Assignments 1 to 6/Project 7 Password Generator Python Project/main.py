import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    characters = ""
    
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "❌ Error: You must select at least one character type."

    # Ensure at least one of each selected type is in the password
    password = []

    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

def main():
    print("🔐 Welcome to the Advanced Password Generator!\n")
    
    try:
        length = int(input("How long do you want the password to be? (min 4 recommended): "))
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (e.g., @, #, !)? (y/n): ").lower() == 'y'

        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        print(f"\n✅ Your generated password:\n🔑 {password}")

    except ValueError:
        print("❌ Invalid input! Please enter a number for password length.")

if __name__ == "__main__":
    main()
