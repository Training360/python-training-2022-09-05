# egy paraméteres függvény, paraméter = argument
# a paraméter nem más, mint egy változó
# függvény definíció
# függvény definícióban lévő paramétert, azaz itt a text-et úgy hívjuk, hogy
# FORMÁLIS PARAMÉTER
def print_hello(text):
    print(f"hello {text}")
    print(text)

print_hello("joe")
# A hívás helyén szereplő paramétert úgy hívjuk, hogy
# AKTUÁLIS PARAMÉTER
print_hello("jack") # hívás helye
# Híváskor az aktuális paraméter ÉRTÉKE bemásolódik a formális paraméterbe
