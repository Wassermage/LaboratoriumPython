# Zadanie 6

try:
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
except:
    print("[!] Podany argument nie jest liczba!")
else:
    print("""
Dostepne operacje:
    add - dodawanie
    sub - odejmowanie
    mul - mnozenie
    div - dzielenie
    mod - reszta z dzielenia
    """)
    operation = input("Wykonywana operacja: ").lower()

    if operation == "add":
        print(f"{a} + {b} = {a+b}")
    elif operation == "sub":
        print(f"{a} - {b} = {a-b}")
    elif operation == "mul":
        print(f"{a} * {b} = {a*b}")
    elif operation == "div":
        if b != 0:
            print(f"{a} / {b} = {a/b}")
        else:
            print("[!] Nie mozna dzielic przez 0!")
    elif operation == "mod":
        print(f"{a} % {b} = {a%b}")
    else:
        print("[!] Nie znaleziono podanej operacji!")
