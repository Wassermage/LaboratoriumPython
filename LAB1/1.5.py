# Zadanie 5

q1 = input("Czy pada deszcz? T/N: ")
q2 = input("Czy na przystanku jest autobus? T/N: ")
raining = True if q1.upper() == "T" else False
busArrived = True if q2.upper() == "T" else False

if raining and busArrived:
    print("Wez parasol!", "Dostaniesz sie na uczelnie!")
elif raining and not busArrived:
    print("Nie dostaniesz sie na uczelnie!")
elif not raining and busArrived:
    print("Dostaniesz sie na uczelnie!", "Milego dnia i pieknej pogody!")
