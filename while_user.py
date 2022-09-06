# A felhasználótól kérjetek be egy számot, és írjátok ki
# a kétszeresét. Ezt egészen addig ismételjétek, amíg
# a felhasználó 0-át nem ír be.

# DRY - don't repeat yourself

#number = int(input("Add meg a számot!"))
number = 100
while not number == 0:   
    number = int(input("Add meg a számot!"))
    print(number * 2)
    