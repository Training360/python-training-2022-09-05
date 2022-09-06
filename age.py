import datetime
# Kérjétek be, hogy a felhasználó mikor született!
# Írjátok ki, hogy ezek alapján hány éves!
# De ne csak egy számot, hanem a következő üzenetet:

# Mivel xxxx-ben születtél, ezért yy éves vagy.

# 1. Kérjük be, hogy mikor született egy változóba! - int-é kell konvertálni
from datetime import datetime


year_of_birth = int(input("Mikor születtél?"))
print(year_of_birth)

# 2. Számoljuk ki, hogy hány éves egy age változóba (2022-ből ki kell vonni!)
#actual_year = 2022
actual_year = datetime.now().year
age = actual_year - year_of_birth
print(age)

# 3. Írjuk ki f-stringgel a megadott üzenetet!
print(f"Mivel {year_of_birth}-ben születtél, ezért {age} éves vagy.")