import random
def check_balance(bal):
    return bal

def deposit(bal, amt):
    bal = bal+amt
    return bal

def withdraw(bal, amt):
    bal = bal-amt
    return bal

print("Hello, Welcome to 'python ATM'")

def ATM():
    bal = random.randint(500,10000)
    atm = True
    while atm:
        choice = int(input("\nSelect what do you want to do?\n1. Checking Balance\n2. Deposit Money\n3. Withdraw Cash\n"))
        if choice == 1:
            print(f"\nYour bank balance is {check_balance(bal)}")
        elif choice == 2:
            amt = int(input("\nEnter your amount to be deposited: "))
            bal = deposit(bal, amt)
            print(f"\nYour bank balance is {check_balance(bal)}")
        elif choice == 3:
            amt = int(input("\nEnter amount (Your denominations should be in 500's only): "))
            if amt%500 == 0:
                if(amt > bal):
                    print(f"Your balance is less then {amt}")
                else:
                    bal = withdraw(bal, amt)
                    print(f"Here is your {amt} take it before it goes back.\n")
                    print(f"Your bank balance is {check_balance(bal)}")
            else:
                print("\nPlease enter your denomination in 500's only")
        else:
            print("Please enter a valid option.")
        choice2 = input("\nDo you want to continue with our services(Y or N) ")
        if choice2 == 'N':
            print("\nThanks for using our ATM.")
            atm = False

ATM()
