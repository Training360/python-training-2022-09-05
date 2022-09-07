# Függvények több paraméterrel
def print_name_times(n, c):
    for i in range(c):
        print(n)

# Írjatok egy print_sum nevű függvényt, mely
# vár egy i és egy j paramétert, és kiírja
# az i és j összegét
# Hívjátok meg előbb 5 és 10 értékkel, majd 8 és 3 értékkel!
def print_sum(i, j):
    print(i + j)

print_name_times("Joe", 5)
print_name_times("Jack", 3)

print_sum(5, 10)
print_sum(3, 8)
