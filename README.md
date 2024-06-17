
# BruteForce Password Attack Demonstration

## Overview
This project demonstrates a brute force attack using a list of commonly used passwords. The program hashes each password in the common password list and checks it against the hashed passwords associated with each username. If a match is found, the program displays the username and the corresponding password.

## Features
- Uses a list of commonly used passwords.
- Compares hashed passwords to those stored in a file.
- Displays matched usernames and passwords.

## Prerequisites
- Python 
- `hashlib` library (included in standard Python library)

## Setup
 Ensure you have the required files:
    - `passwords.txt`: Contains a list of commonly used passwords.
    - `usernames.txt`: Contains usernames and their hashed passwords in the format `username:hashed_password`.

## Usage
Run the script to perform the brute force attack


