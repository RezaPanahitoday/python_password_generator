import string
import random
#Ask user for password length
len_password = int(input("Enter password length: "))
# allowed characters
charcts = string.ascii_letters + string.digits + string.punctuation
password = ""
for _ in range(len_password):
    password += random.choice(charcts)
print(password)