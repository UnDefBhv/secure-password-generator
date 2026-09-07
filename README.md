# Secure Password Generator

A secure password generator built with Python and the `secrets` module. It generates strong passwords using cryptographically secure randomness and checks whether the generated password has appeared in known data breaches.

## Features

* Cryptographically secure random generation
* Custom password length
* Uppercase and lowercase letters
* Numbers
* Special characters
* Minimum length validation
* Uses Python's `secrets` module instead of `random`
* Checks generated passwords against known data breaches
* Uses the Have I Been Pwned Pwned Passwords API
* Uses k-anonymity to avoid sending the complete password or hash

## Requirements

* Python 3.8 or newer
* Internet connection for breach checking

## Usage

Clone the repository:

```bash
git clone https://github.com/UnDefBhv/secure-password-generator
cd secure-password-generator
```

Run the program:

```bash
python3 password_generator.py
```

Enter the desired password length:

```text
Password length: 16

Generated password:
x7!Kp2@Lm9#Qa4$Z

This password was not found in known breaches.
```

If the generated password has appeared in known breaches:

```text
Warning: this password has appeared in 12 breaches.
```

## Technologies

* Python
* `secrets`
* `string`
* `hashlib`
* `urllib.request`
* Have I Been Pwned Pwned Passwords API

## Security

The project uses Python's `secrets` module, which is designed for generating cryptographically strong random values.

The generated password is hashed locally using SHA-1 before the breach check. Only the first 5 characters of the hash are sent to the Pwned Passwords API using k-anonymity.

The generated passwords are not stored in files or databases.

## License

Licensed under the Apache License 2.0.
