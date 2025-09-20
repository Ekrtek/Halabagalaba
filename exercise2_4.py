matka = int(input("Matka-ajon kilometrit: \n"))
kapunki = int(input("Kapunki-ajon kilometrit: \n"))
matka_kulu = 5.1 / 100
kapunki_kulu = 7.5 / 100
kulutus = (matka * matka_kulu) + (kapunki * kapunki_kulu)
kulutus = round(kulutus, 2)
print(f"Kulutus: {kulutus} l")