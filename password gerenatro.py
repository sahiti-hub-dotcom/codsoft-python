import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    print("==================")

    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
