money = int(input("Anna rahaa: \n"))
price = int(input("Ostosten hinta: \n"))

if price < money:
    leftover = money - price
    print(f"Kiitos. Annetaan takaisin {leftover} €")
elif price == money:
    print("Kiitos.")
elif money < price:
    more_money = int(input("Rahat eivät riitä, anna lisää rahaa: \n"))
    money += more_money
    if money < price:
        print("Sinulla ei ole tarpeeksi rahaa")
    else:
        leftover = money - price
        print(f"Kiitos. Annetaan takaisin {leftover} €")