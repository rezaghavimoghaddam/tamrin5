import math

def Quadratic_Equation():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))
    r = (b*b) - (4*(a*c))
    m = math.sqrt(r)

    x = (b + m) / (a * 2)

    print(x)

Quadratic_Equation()