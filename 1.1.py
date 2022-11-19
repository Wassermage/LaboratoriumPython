# Zadanie 1

x = float(input("Podaj x: "))

def a(x):
    if x > 0:
        return 2 * x
    elif x < 0:
        return -3 * x
    else:
        return 0

def b(x):
    if x >= 1:
        return x ** 2
    else:
        return x

def c(x):
    if x > 2:
        return x + 2
    elif x < 2:
        return x - 4
    else:
        return 8

print(f"a({x}) = {a(x)}")
print(f"b({x}) = {b(x)}")
print(f"c({x}) = {c(x)}")
