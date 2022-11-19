# Zadanie 4.3

tab = []

for i in range(6):
    tab.append([((i % 2 + j % 2) % 2) for j in range(6)])

for line in tab:
    print(line)
