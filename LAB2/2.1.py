# Zadanie 1
# base? -> base10


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
            power = len(number)-1
            numBase10 = 0

            for digit in number:
                digit = int(digit)
                if digit < base:
                    numBase10 += digit*base**power
                    power -= 1
                else:
                    print(f"[!] Podana liczba nie jest zapisana w systemie base{base}!")
                    exit()

            print(f"{number}({base}) = {numBase10}(10)")
