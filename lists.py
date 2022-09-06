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
# 2. Írd ki, hogy "Az év egyik hónapja január." az első három hónappal!
# 3. Hozz létre egy listát a 3, 7, 9, 13 számokkal! Add össze a listában
# lévő számokat!

numbers = [3, 7, 9, 13]
for number in numbers:
    print(number)