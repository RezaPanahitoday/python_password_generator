import random
import string 

class Password:
    def __init__(self, length):
        self.length = length


    def generate(self):

        chart = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]

        for _ in range(self.length - 4):
            password.append(random.choice(chart))

        
        final_password =''.join(password)
        return final_password


# length = int(input("Enter password length:"))
# my_password = Password(length)
# print(my_password.generate())