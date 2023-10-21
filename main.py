def Rupeeto(c1_amt,c2):
    if c2 == "Dollars":
        res = c1_amt*0.012
    elif c2 == "Euros":
        res = c1_amt*0.011
    elif c2 == "Yen":
        res = c1_amt*1.81
    print(f"Your converted amount is {res} {c2}")

def Dollarsto(c1_amt,c2):
    if c2 == "Rupees":
        res = c1_amt*83.24
    elif c2 == "Euros":
        res = c1_amt*0.94
    elif c2 == "Yen":
        res = c1_amt*149.86
    print(f"Your converted amount is {res} {c2}")

def Eurosto(c1_amt,c2):
    if c2 == "Rupees":
        res = c1_amt*88.27
    elif c2 == "Dollars":
        res = c1_amt*1.06
    elif c2 == "Yen":
        res = c1_amt*158.91
    print(f"Your converted amount is {res} {c2}")

def Yento(c1_amt,c2):
    if c2 == "Rupees":
        res = c1_amt*0.56
    elif c2 == "Dollars":
        res = c1_amt*0.0067
    elif c2 == "Euros":
        res = c1_amt*0.0063
    print(f"Your converted amount is {res} {c2}")

def convert():
    print("Welcome to currency converter.")
    c1 = input("Enter the name of currency you want to convert: ")
    c1_amt = float(input("Enter your amount: "))
    available_currencies = ["Rupees", "Dollars", "Euros", "Yen"]
    cnt = True
    print("\n")
    for i in available_currencies:
        print(i)
    while cnt:
        c2 = input("\nSelect the name of currency you want to convert into: ")
        if c1 == "Rupees":
            Rupeeto(c1_amt,c2)
        elif c1 == "Dollars":
            Dollarsto(c1_amt,c2)
        elif c1 == "Euros":
            Eurosto(c1_amt,c2)
        elif c1 == "Yen":
            Yento(c1_amt,c2)
        cho = input("Do you want to continue(Y or N): ")
        if cho == "N":
            cnt = False

convert()