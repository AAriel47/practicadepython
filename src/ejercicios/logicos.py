import os

# Limpia la consola
os.system('cls' if os.name == 'nt' else 'clear')

print(1 < 2 | 3 > 2)
print(not 1 < 2)
print((1 < 2) & (3 > 2))