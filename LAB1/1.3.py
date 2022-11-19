# Zadanie 3

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a != 0:
    delta = b**2 - 4*a*c

    if delta == 0:
        x1 = x2 = -b/(2*a)
        print(f"x = {x1}")
    elif delta > 0:
        x1 = (-b - delta**(1/2))/(2*a)
        x2 = (-b + delta**(1/2))/(2*a)
        print(f"x1 = {x1}\nx2 = {x2}")
    else:
        print("[!] delta<0")
else:
    print("[!] a=0")
