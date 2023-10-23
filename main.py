def fahrenheit(tem):
    res = ((tem*9)/5)+32
    print(f"{tem} degree celsius is {res} fahrenheit")

def celsius(tem):
    res = ((tem-32)*5)/9
    print(f"{tem} fahrenheit is {res} degree celsius")

unit = input("Enter your preferred units of temperature(celsius or fahrenheit): ")
tem = float(input("Enter temperature: "))
if unit == "fahrenheit":
    celsius(tem)
elif unit == "celsius":
    fahrenheit(tem)