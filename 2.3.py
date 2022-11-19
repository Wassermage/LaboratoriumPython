# Zadanie 3
# base10 -> base?


digits = "0123456789abcdef"

try:
    numBase10 = int(input("Podaj liczbe: "))
    base = int(input("Podaj podstawe: "))
except:
    print("[!] Podana wartosc musi byc liczba calkowita!")
else:
    if (base < 2 or base > 10) and base != 16:
        print("[!] Dozwolone systemy liczbowe: 2, ..., 10, 16")
    else:
        numBaseOther = ""
        while True:

            numBaseOther += digits[numBase10 % base]
            numBase10 //= base

            if numBase10 == 0:
                break

        numBaseOther = numBaseOther[::-1]
        print(numBaseOther)



