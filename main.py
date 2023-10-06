def add(a, b):
    return (a+b)

def sub(a, b):
    return (a-b)

def mul(a, b):
    return (a*b)

def div(a, b):
    return (a/b)

from art import logo

def cal():

    print(logo)
    a = float(input("Enter your number: "))
    operation = {
        '+' : add,
        '-' : sub,
        '*' : mul,
        '/' : div
    }
    for i in operation:
        print(i)
    con = True

    while con:
        sel_op = input("Enter your operation: ")
        b = float(input("Enter your second number: "))
        res = operation[sel_op](a,b)
        print(f"{a} {sel_op} {b} = {res}")
        repeat = input("Do you want to continue? (y or n) ")

        if repeat == 'y':
            a = res
        else:
            con = False

cal()