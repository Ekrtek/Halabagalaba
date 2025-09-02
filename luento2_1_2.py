# pelkkä print() tulostaa aina yhden \n vakiona
# tekstiä voi tulostaa eri riveille käyttämällä \n,
# voi ketjuttaa useamman peräkkäin jos haluaa.
print("halabagalaba\n\nTämä tulee toiselle riville")
print()
print("Testi")

# \t sarkain (englanniksi tab)
print("Lasku:\t\t350 €")
print("Korko:\t\t5%")
print("Päivämäärä:\t2.9.2025")
#VAIHE 1: pyydetään käyttäjälyä säästöt ja muutetaan desimaaliluvuksi.
#kysytään käyttäjältä säästöt ja muutetaan desimaaliluvuksi
savings = float(input("Kuinka paljon sinulla on säästöjä?\n"))

print(savings)


# kysytään käyttäjältä myös viime kuun palkka
salary = float(input("Kuinka paljon sait tässä kuussa palkkaa?\n"))
print(salary)

# vaihe 2: ohjelman laskukaava / logiikka
# korkokerroin, +5%
increase = 1.05

# Lasketaan lopputulos
total = (savings + salary) * increase
# Vaihe 3: tulostetaan lopputulos mukavassa muodossa
# loppukäyttäjälle
# teknisesti on mahdollista tehdä aaltosulkeiden sisällä myös laskutoimituksia
# esim. {total * increase}, mutta lähtökohtaisesti nämä ratkaisut ovat
# aika vaikeaselkoisia, koska koodi ahtaa kaiken logiikan yhteen koodiriviin.
print(f"Uusi summa korkojen jälkeen: {total}€")
