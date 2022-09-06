# Kérjétek be a felhasználó nevét!
# Kérjétek be, hogy hányszor kerüljön kiírásra!
# Joe 3
# Írjátok ki annyiszor a felhasználó nevét!
# JoeJoeJoe
# Aki ügyes:
# Joe Joe Joe

# Kérjétek be a felhasználó nevét!
name = input("Mi a neved?")  # str "István"

# Kérjétek be, hogy hányszor kerüljön kiírásra! - egész szám!
count = int(input("Hányszor írjam ki?")) # str "10" -> 10

# Írjuk ki a nevet a számszor!
print(name * count)

#name += " "
#print(name * count)

print((name + " ") * count)

print("*" + name + "*")