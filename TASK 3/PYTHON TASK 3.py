import string
import random

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            break
        except ValueError as e:
            print(e)

    # Generate the password
    password = generate_password(length)

    # Display the password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

