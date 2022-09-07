# Írjátok meg a signum függvényt! Egy paramétere van, ami egy szám.
# Ha a szám kisebb, mint 0, akkor -1-et vissza
# Ha 0, akkor 0-át ad vissza
# Ha nagyobb, mint 0, akkor 1-et ad vissza
def signum(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1

# Írjatok egy függvényt, ami vár egy egész számot, és visszaadja
# annak abszolútértékét!
def abs(n):
    if n < 0:
        return -n
    else:
        return n


# Struktúrált programozás: minden függvényben CSAK egy
# return utasítás lehet
def abs_structured(n):
    if n < 0:
        result = -n
    else:
        result = n
    return result

# Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
# visszaadja a területet!
def area(a, b):
    return a * b

# Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
# visszaadja a kerületet!
def calculate_perimeter(a, b):
    return 2 * (a + b)


# Írjatok egy függvényt, amely vár két számot, és visszaadja a
# kettő közül a nagyobbat!
def max(a, b):
    if a > b:
        return a
    else:
        return b


# Vár egy számot és visszaadja a "páros" szöveget, ha páros,
# ellenkező esetben hogy "páratlan"
def get_type(n):
    if n % 2 == 0:
        return "páros"
    else:
        return "páratlan"

def get_type_structured(n):
    if n % 2 == 0:
        type = "páros"
    else:
        type = "páratlan"
    return type


# Ha a függvény boolean értéket ad vissza, akkor 
# logikai függvény: True, vagy False

# Írj egy is_even nevű függvényt, mely a paraméteréről
# eldönti, hogy páros-e!
# True-t adjon vissza, ha páros, False értéket adjon vissza,
# ha páratlan
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Egyszerűbben így írható:
def is_even_simple(n):
    return n % 2 == 0

print(signum(30))

print(abs(10))
print(abs(-20))

print(abs_structured(10))
print(abs_structured(-20))

print(area(10, 5))
print(area(3, 2))

print(calculate_perimeter(4, 6))
print(calculate_perimeter(3, 5))

print(max(6, 9))
print(max(5, 5))
print(max(10, 4))

print(get_type(5))
print(get_type(6))


if is_even(10):
    print("Ez egy szép páros szám")
else:
    print("Ez egy páratlan szám")