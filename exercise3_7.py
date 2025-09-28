package = input("Kirje vai paketti? k/p \n")
weight = input("Lähetyksen paino grammoina? \n")
weight = int(weight)
# lähdemme tästä laskemaan painoja sekä kirjeille että paketeille
# monta riviä koska en ole varma miten olisi parempi tehdä
letter_weight = (weight // 100) / 100
if 200 <= weight <= 500:
    letter_pay = 0.5 + letter_weight * 4
    letter_pay = round(letter_pay, 2)
elif weight < 200:
    letter_pay = 0.5
else:
    letter_pay = 0.5 + letter_weight * 7
    letter_pay = round(letter_pay, 2)
# tehty paketeille omat muuttujat ja muuttujoille niiden määritelmät
box_weight = weight // 100 / 100
if 200 <= weight <= 500:
    box_pay = 2 + box_weight * 8
elif weight < 200:
    box_pay = 2
else:
    box_pay = 2 + box_weight * 14
# lähdetään selvittää onko kirje vai paketti ja sen mukaan printtaamme hinnat.
if package == "k":
    if weight > 500:
        postbox = input("Mahtuuko kirje postilaatikkoon? k/e \n")
        if postbox == "k":
            print(f"Lähetyksen hinta: {letter_pay}€\n")
        elif postbox == "e":
            letter_pay = letter_pay + 2
            print(f"Lähetyksen hinta: {letter_pay}€ \n")
    else:
        print(f"Lähetyksen hinta: {letter_pay}€ \n")
else:
    print(f"Lähetyksen hinta: {box_pay}€ \n")