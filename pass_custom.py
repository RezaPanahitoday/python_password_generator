import random
import string 

class CustomPassword:
    def __init__(self, length, lower, upper, digits, symbols):
        self.length = length
        self.lower = lower
        self.upper = upper
        self.digits = digits
        self.symbols = symbols

    def conditions(self):
        password = ""         #allowed characters
        final_password = []   #final password characters

        if self.lower == "y":
            password += string.ascii_lowercase
        if self.upper == "y":
            password += string.ascii_uppercase
        if self.digits == "y":
            password += string.digits
        if self.symbols == "y":
            password += string.punctuation

        if not password:
            return "Error: No character types selected!"

        for _ in range(self.length):
            final_password.append(random.choice(password))
    
        my_password =''.join(final_password)
        return my_password


# lower = input("Lower?(y/n): ")
# upper = input("Upper?(y/n): ")
# digits = input("Digits?(y/n): ")
# symbols = input("Symbols?(y/n): ")



# length = int(input("Enter password length:"))
# my_password = CustomPassword(length, lower, upper, digits, symbols)
# print(my_password.conditions())