from Pass_Custome import CustomPassword
from Pass_Simple import Password


print("1. Custome password")
print("2. Simple password")
mode = input("Enter, just number(1/2):")

if mode == "1" :
    lower = input("Lower?(y/n): ")
    upper = input("Upper?(y/n): ")
    digits = input("Digits?(y/n): ")
    symbols = input("Symbols?(y/n): ")

    length = int(input("Enter password length:"))
    my_password = CustomPassword(length, lower, upper, digits, symbols)
    print(my_password.conditions())

elif mode == "2":
    length = int(input("Enter password length:"))
    my_password = Password(length)
    print(my_password.generate())
else:
    print("Invalid input!")