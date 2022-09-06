# Írjuk ki 5x egymás után a nevünket
#print("István\n" * 5)

# i, j, k
for i in range(5):
    print(i)
    print("István")
print("End")

# Feladat: Írj egy ciklust, ami kíírja a számokat 1-től 100-ig egymás alá!
for i in range(100):
    print(i + 1)


# Feladat: Írd ki egymás után a neved 5x, írd elé a sorszámot is!
for i in range(5):
    print(f"{i + 1}. István")
    #print(str(i + 1) + ". István")

# Feladat: Írj egy ciklust, amely 1-től 10-ig kiíírja a számokat és azok 
# négyzetét is egy új sorba!
for i in range(10):
    j = i + 1
    result = j ** 2
    print(f"A {j} szám négyzete: {result}")

# i felveszi a következő értékeket: 5 <= i < 10
for i in range(5, 10):
    print(i)

# harmadik paraméter a lépés
for i in range(10, 20, 2):
    print(i)

# lépés negatív szám, csökkenti, esetünkben 10-től 1-ig
for i in range(10, 0, -1):
    print(i)
