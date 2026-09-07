import secrets
import string
import hashlib
import urllib.request


def check_password_breach(password):
    password_hash = hashlib.sha1(
        password.encode("utf-8")
    ).hexdigest().upper()

    prefix = password_hash[:5]
    suffix = password_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Secure-Password-Generator"
        }
    )

    with urllib.request.urlopen(request) as response:
        data = response.read().decode("utf-8")

    for line in data.splitlines():
        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return int(count)

    return 0


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

    count = check_password_breach(password)

    if count:
        print(f"\nWarning: this password has appeared in {count} breaches.")
    else:
        print("\nThis password was not found in known breaches.")

except ValueError as error:
    print(f"\nError: {error}")

except urllib.error.URLError:
    print("\nError: unable to check the password database.")
