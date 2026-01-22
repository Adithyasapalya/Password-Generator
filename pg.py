import random
import string

def generate_password(min_len, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


generate_password(10)