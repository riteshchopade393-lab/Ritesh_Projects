import random as r
import string as s

def generate_password(length):
    characters = s.ascii_letters + s.digits + s.punctuation
    password = ""

# def generate_password(length):
#     characters = s.ascii_letters + s.digits + s.punctuation
#     password = ""

    for _ in range(length):
        password += r.choice(characters)

    return password

# password strength checker

def check_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in s.punctuation for char in password)
    
    strength_score = sum([has_upper, has_lower, has_digit, has_symbol])

    if len(password) < 8 or strength_score <= 2:
        return("Weak ❌")
    elif len(password) < 12 or strength_score == 3:
        return("Medium ⚠️")
    else:
        return("Strong ✅")

# Main program 

while True:
    print("\n--- Password Generate ---")
    length = input("Enter password (or q means exit): ")

    if length.lower() == 'q':
        print("Existing Password Generator. Goodbye ")
        break
    
    if not length.isdigit() or int(length) < 4:
        print("Please enter valid number (minimum 4): ")
        continue

    length = int(length)

    password = generate_password(length)
    strength = check_strength(password)

    print("\n Generate password: ", password)
    print("Password strength : ", strength)
    

        
        
    
    


