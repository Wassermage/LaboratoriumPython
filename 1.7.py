# Zadanie 7

ch = input("Podaj znak: ")

def charconvert(ch):
    if ch[0].isupper():
        return ch[0].lower()
    else:
        return ch[0].upper()

print(charconvert(ch))
