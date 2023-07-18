import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nlet = int(input("How many letters would you like in your password?\n"))
nnum = int(input(f"How many numbers would you like?\n"))
nsym = int(input(f"How many symbols would you like?\n"))

password = []

for char in range(1, nlet + 1):
    password.append(random.choice(letters))
    
for char in range(1, nnum + 1):
    password += random.choice(numbers)
    
for char in range(1, nsym + 1):
    password += random.choice(symbols)
    
random.shuffle(password)

PASSWORD = ""

for char in password:
    PASSWORD += char
    
print(f"Your password is: {PASSWORD}")
print("Thank you for using the PyPassword Generator!")
print("Have a nice day!")