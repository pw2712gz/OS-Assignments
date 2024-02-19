import itertools
import time
import string
import random

# Function to generate a random password
def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Function to brute-force guess the password
def guess_password(target, chars):
    start_time = time.time()
    guesses = 0
    for password in itertools.product(chars, repeat=len(target)):
        guesses += 1
        if ''.join(password) == target:
            return guesses, time.time() - start_time

# Characters sets
uppercase_chars = string.ascii_uppercase
expanded_chars = string.ascii_letters + string.digits + ':;><=?@{|}\\^_`'

# Generate passwords
password_upper = generate_password(4, uppercase_chars)
password_expanded = generate_password(4, expanded_chars)

# Guess passwords
guesses_upper, time_upper = guess_password(password_upper, uppercase_chars)
guesses_expanded, time_expanded = guess_password(password_expanded, expanded_chars)

# Output results to a file
with open("password_guess_results.txt", "w") as f:
    f.write("Asg3 SampleOutput Assignment #3 for ICS 462 by Ayub Yusuf\n\n")
    f.write(f"Generated password is: {password_upper}\n")
    f.write(f"Found the password after {guesses_upper} guesses.\n")
    f.write(f"It took {time_upper:.6f} seconds to find the password.\n\n")
    f.write(f"Generated password is: {password_expanded}\n")
    f.write(f"Found the password after {guesses_expanded} guesses.\n")
    f.write(f"It took {time_expanded:.6f} seconds to find the password.\n\n")
    f.write(f"It took {time_expanded / time_upper:.2f} times as long with the expanded character set to guess the password.\n")

print("Program completed.")
