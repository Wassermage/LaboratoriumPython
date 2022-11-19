# Zadanie 2
# base? -> base10 przy uzyciu schematu Hornera


try:
    number = str(int(input("Podaj n: "))) # int() dodane w celu zabezpieczenia przed podaniem niepoprawnych znakow
except:
    print("[!] Niepoprawna liczba")
else:
    try:
        base = int(input("Podstawa: "))
    except:
        print("[!] Podstawa musi byc liczba calkowita!")
    else:
        if base < 2 or base > 10:
            print("[!] Podstawa musi byc liczba z zakresu 2-10")
        else:
            numBase10 = 0
            for i, digit in enumerate(number):
                numBase10 = numBase10 * base + int(digit)
            print(numBase10)
