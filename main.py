import random
import string

# Function to generate a random password with specified length and criteria
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    # Define character sets for each criteria
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    lowercase_chars = string.ascii_lowercase if use_lowercase else ""
    digit_chars = string.digits if use_digits else ""
    special_chars = "!@#$%^&*()_+=-[]{}|;:'\",.<>?/" if use_special_chars else ""
    # Combine character sets based on selected criteria
    all_chars = uppercase_chars + lowercase_chars + digit_chars + special_chars

    # Check if at least one criteria is selected
    if not all_chars:
        return "Please select at least one criteria."

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    print(f"Your generated password is: {password}")
  
