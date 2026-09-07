# Secure Password Generator

A secure password generator built with Python and the `secrets` module. It generates strong passwords using cryptographically secure randomness.

## Features

* Cryptographically secure random generation
* Custom password length
* Uppercase and lowercase letters
* Numbers
* Special characters
* Minimum length validation
* Uses Python's `secrets` module instead of `random`

## Requirements

* Python 3.8 or newer

## Usage

Clone the repository:

```bash
git clone https://github.com/UnDefBhv/secure-password-generator
cd secure-password-generator
```

Run the program:

```bash
python password_generator.py
```

Enter the desired password length:

```text
Password length: 16

Generated password:
x7!Kp2@Lm9#Qa4$Z
```

## How it works

The program first generates one character from each required character set:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

It then fills the remaining positions and securely shuffles the characters before displaying the final password.

## Security

The project uses Python's `secrets` module, which is designed for generating cryptographically strong random values.

The generated passwords are not stored in files or databases.

## License

Licensed under the Apache License 2.0.
