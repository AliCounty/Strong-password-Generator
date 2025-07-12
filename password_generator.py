
import random
import string


def generate_password(length=12):
    if length < 6:
        return "Password length is too short. Please use at least 6 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        user_length = int(input("Enter the desired password length: "))
        print("Your generated password:")
        print(generate_password(user_length))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

