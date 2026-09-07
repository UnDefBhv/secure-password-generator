import secrets
import string


def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    characters = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


try:
    length = int(input("Password length: "))

    password = generate_password(length)

    print("\nGenerated password:")
    print(password)

except ValueError as error:
    print(f"\nError: {error}")
