# Literálok


10 # Egész literál

200000 # Egész literál, nehezen olvasható

200_000 # Jól olvasható karakteres literál

3.14 # Lebegőpontos literál

"hello" # String/szöveges/karakterlánc literál

'hello' # Ez is String literál, csak más a határolójel

True # Igaz logikai literál (vigyázzunk a kis- és nagybetűkre)

False # Hamis logikai literál

# Literáloknak van típusa
# Python típusos programozási nyelv

# Típus lekérdezhető a type függvénnyel

type(10) # név - és zárójelek között a paraméter lista - ez egy függvény
# lehet 0, 1 vagy több paraméter
# visszatérési érték elveszik

print("hello") # print egy függvény, melynek átadtunk egy paraméterül szöveges literált

# Függvényeket láncolni lehet

print(type(10)) # int - integer - egész szám
print(type(1.1)) # float - lebegőpontos szám
print(type("hello")) # str
print(type(True)) # bool - boolean - logikai

# Változódeklaráció: név - kezdőérték

course = "Kezdő Python"
print(course)

# Második változó létrehozása
age = 25
print(age)

# Változó: értéke módosítható, felülírjuk az eredeti értékét
age = 26
print(age)

#print(color) # NameError: name 'color' is not defined

# Konvenció szerint a szavakat aláhúzásjellel választjuk el
employee_name = "John Doe"

# Változónév betűvel kezdődjön, pl. a 7number nem megfelelő

# Egy változó törölhető
print(employee_name)

#del(employee_name) # Változó törölhető, nem használjuk!
#print(employee_name)

print(type(course))
print(type(age))

# Változtatható-e a változó típusa?

favourite_number = 20
print(favourite_number)
favourite_number = "húsz"
print(favourite_number)

# Pythonban igen, de ne használjuk

# Vannak foglalt kulcsszavak, nem használhatjuk változónévként
