# Zadanie 4.2

n = int(input("Podaj n: "))
tab = []
for i in range(n):
    tab.append([i, i**2])

for i in range(len(tab)):
    print(tab[i])
