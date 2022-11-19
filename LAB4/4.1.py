# Zadanie 4.1
import random

list1 = []
list2 = []
list3 = []
for i in range(4):
    list1.append(random.randint(0, 99))
    list2.append(random.randint(0, 99))

list1.sort()
list2.sort()
print(f"Lista #1: {list1}")
print(f"Lista #2: {list2}")

list3 = list1 + list2
list3.sort()

print(f"Lista #3: {list3}")
