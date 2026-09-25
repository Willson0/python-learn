import random

def generate_password():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*"

    chars = (
        random.choices(letters, k=3)
        + random.choices(digits, k=3)
        + random.choices(symbols, k=2)
    )
    random.shuffle(chars)

    password = ""
    for char in chars:
        password += char
    return password

print(generate_password())
