# Problem Statement
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)





import hashlib

def hash_password(password: str) -> str:
    """
    Takes in a password and returns its SHA256 hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Checks if the hash of the provided password matches the stored hash for the given email.
    """
    hashed_input = hash_password(password_to_check)
    stored_hash = stored_logins.get(email)
    
    return hashed_input == stored_hash

# Example usage
def main():
    stored_logins = {
        "user1@example.com": hash_password("password123"),
        "admin@example.com": hash_password("supersecure"),
        "me@abc.com": hash_password("letmein")
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("✅ Login successful!")
    else:
        print("❌ Login failed. Incorrect email or password.")

if __name__ == "__main__":
    main()
