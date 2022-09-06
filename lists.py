from re import M


names = ["Joe", "Jack", "Jane"]

# végigiterálunk a names változó elemein
for name in names:
    print(name)

# enumerate függvényt kell használni, ha az indexhez hozzá szeretnénk férni
for i, name in enumerate(names):
    print(i)
    print(name)

counter = 10
for name in names:
    print(counter)
    print(name)
    counter += 2

# 1. Írd ki az első három hónap nevét egymás alá!
months = ["január", "február", "március"]
for month in months:
    print(month)

lista = ["január", "február", "március"]
for ciklusvaltozo in lista:
    print(ciklusvaltozo)

ciklusvaltozo = "január"
print(ciklusvaltozo)
ciklusvaltozo = "február"
print(ciklusvaltozo)
ciklusvaltozo = "március"
print(ciklusvaltozo)

# 2. Írd ki, hogy "Az év egyik hónapja xxx." az első három hónappal!
months = ["január", "február", "március"]
for month in months:
    print(f"Az év egyik hónapja {month}.")

# 3. Hozz létre egy listát a 3, 7, 9, 13 számokkal! Add össze a listában
# lévő számokat!

# Írj egy ciklust, amely összeadja a listában szereplő 
# összes számot egy `sum` változóba! 
# A `sum` változónak 0 értéket kell adnod az összegzés előtt,
#  majd a ciklus befejezése után az `sum` változó értékét írasd ki!

numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    sum += number
print(sum)

numbers = [3, 7, 9, 13]
sum = 0 # 0
number = 3
sum += number # 0 + 3 = 3
number = 7
sum += number # 3 + 7 = 10
number = 9
sum += number # 10 + 9 = 19
number = 13
sum += number # 19 + 13 = 32
print(sum)


numbers = [3, 7, 9, 13]
for number in numbers:
    print(number)