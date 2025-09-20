import random
arvottu = random.randint(1, 10)
print(f" Arvottu luku: {arvottu}")
side_a = random.randint(2, 10)
side_b = random.randint(2, 10)
print(f"Arvottu 1. sivu: {side_a}")
print(f"Arvottu 2. sivu: {side_b}")
total = side_a * side_b
print(f"Arvotuista sivuista laskettu pinta-ala: {total}")