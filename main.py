import random

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!','@','#','$','%','&','*']
cap = int(input("Enter the number of Capital letters required for your password: "))
sma = int(input("\nEnter the number of small letters required for your password: "))
num = int(input("\nEnter the number of numerical characters required for your password: "))
sp = int(input("\nEnter the number of special characters required for your password: "))
newpass = True

while newpass:
    password = []
    for _ in range(cap):
        random.shuffle(capital)
        password += random.choice(capital)
        
    for _ in range(sma):
        random.shuffle(small)
        password += random.choice(small)
        
    for _ in range(num):
        random.shuffle(number)
        password += random.choice(number)
        
    for _ in range(sp):
        random.shuffle(special)
        password += random.choice(special)
        
    shupass = True
    while shupass:
        random.shuffle(password)
        res = ''.join(password)
        print(f"\nyour password is '{res}'")
        choice = input("Do you want to shuffle your password? (Y or N) ")
        if choice == 'N':
            shupass = False
    choice2 = input("\nDo you want another password? (Y or N) ")
    if choice2 == 'N':
        newpass = False
print(f"\nYour final password is {res}")