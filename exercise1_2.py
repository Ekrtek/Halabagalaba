price = float(input("Hinta ilman ALV:\n"))
alv = 1.255
total = round((price * alv), 2)
print(f"Hinta ALV kanssa:{total}€")
