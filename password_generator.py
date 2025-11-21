import string
import random
# Get password length from user
len_password = int(input("Enter password length: "))

# All possible characters
all_chars = string.ascii_letters + string.digits + string.punctuation

# Initialize password list with at least one of each type
password = [
    random.choice(string.ascii_lowercase),   # ensure lowercase
    random.choice(string.ascii_uppercase),   # ensure uppercase
    random.choice(string.digits),            # ensure digit
    random.choice(string.punctuation)        # ensure symbol
]

# Fill the rest of the password length with random characters
for _ in range(len_password - 4):
    password.append(random.choice(all_chars))
random.shuffle(password)   # shuffle to mix characters

# Convert list to string
final_password = ''.join(password)
print(final_password)