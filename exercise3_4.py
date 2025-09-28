money = input("Anna rahaa: \n")
money = int(money)
price = input("Ostosten hinta: \n")
price = int(price)
# selvitämme onko käyttäjällä tarpeeksi rahaa sekä onko lisätä jos ei ole
if price < money:
    leftover = money - price
    print(f"Kiitos. Annetaan takaisin {leftover} €")
elif price == money:
    print("Kiitos.")
elif money < price:
    more_money = input("Rahat eivät riitä, anna lisää rahaa: \n")
    more_money = int(more_money)
    money += more_money
    if money < price:
        print("Sinulla ei ole tarpeeksi rahaa")
    else:
        leftover = money - price
        print(f"Kiitos. Annetaan takaisin {leftover} €")