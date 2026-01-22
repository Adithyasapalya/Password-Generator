import random
import string

def generate_password(min_len, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special
        
    pwd = " "
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len (pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_numbers
        if special_chars:
            meet_criteria = meet_criteria and has_special

    return pwd

min_len = int(input("Enter the minimum length:"))
has_number = input("Do you want numbers? (y/n): ").lower() == "y"
has_special = input("Do you want special characters? (y/n): ").lower() == "y"

pwd = generate_password(min_len, has_number,has_special)
print("The Generated Password is:", pwd)