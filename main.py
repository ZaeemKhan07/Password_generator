import random
import sys

# Global lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(nr_letters, nr_symbols, nr_numbers):
    password_list = []

    # Using .append() is safer than += for single items
    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))

    for char in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    # --- CRITICAL FIX IS HERE ---
    password = "" 
    # Ensure there is NO comma at the end of the line above
    
    for char in password_list:
        password += char
    
    return password

if __name__ == "__main__":
    # 1. N8N AUTOMATION CHECK
    # If N8N sends arguments (letters, symbols, numbers), use them automatically.
    if len(sys.argv) > 3:
        nr_letters = int(sys.argv[1])
        nr_symbols = int(sys.argv[2])
        nr_numbers = int(sys.argv[3])
    
    # 2. MANUAL VS CODE CHECK
    # If no arguments are sent, ask the user (for testing locally).
    else:
        print("Welcome to the PyPassword Generator!")
        nr_letters = int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Generate and print
    final_password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(final_password)
