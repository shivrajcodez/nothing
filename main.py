import random
import string
import re

branch-29
boom
it done
=======
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.?/"

    if not characters:
        return None

    password = []

    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{};:,.?/"))

    remaining = length - len(password)

    if remaining > 0:
        password += random.choices(characters, k=remaining)

    random.shuffle(password)

    return ''.join(password)


def check_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_\-+=\[\]{};:,.?/]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    print("=" * 45)
    print("      PASSWORD GENERATOR & STRENGTH CHECKER")
    print("=" * 45)

    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                length = int(input("Enter password length (minimum 6): "))

                if length < 6:
                    print("Password length must be at least 6.")
                    continue

                upper = input("Include uppercase letters? (y/n): ").lower() == "y"
                lower = input("Include lowercase letters? (y/n): ").lower() == "y"
                digits = input("Include numbers? (y/n): ").lower() == "y"
                symbols = input("Include special characters? (y/n): ").lower() == "y"

                password = generate_password(
                    length,
                    upper,
                    lower,
                    digits,
                    symbols
                )

                if password is None:
                    print("Please select at least one character type.")
                    continue

                strength, suggestions = check_strength(password)

                print("\n" + "-" * 45)
                print("Generated Password:", password)
                print("Strength:", strength)
                print("-" * 45)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            password = input("\nEnter password to check: ")

            strength, suggestions = check_strength(password)

            print("\n" + "-" * 45)
            print("Password Strength:", strength)
            print("-" * 45)

            if suggestions:
                print("\nSuggestions:")
                for suggestion in suggestions:
                    print("•", suggestion)
            else:
                print("Your password meets all basic strength requirements.")

        elif choice == "3":
            print("\nThank you for using Password Generator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    m
