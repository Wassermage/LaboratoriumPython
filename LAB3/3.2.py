# Zadanie 3.2

n1 = str(input("Podaj n1: "))
n2 = str(input("Podaj n2: "))

n1 = n1[::-1]
n2 = n2[::-1]

n3 = ""
addToNextDigit = 0

for i in range(max(len(n1), len(n2)) + 1):
    digit1 = int(n1[i] if i < len(n1) else 0)
    digit2 = int(n2[i] if i < len(n2) else 0)

    n3 += str((digit1 + digit2 + addToNextDigit) % 10)
    addToNextDigit = (digit1 + digit2 + addToNextDigit) // 10

n3 = n3[::-1]
print(n3)

