from datetime import date, datetime, timedelta

# tästä päivästä vuoden loppuun aikaleimat
first = date(year=2025, month=9, day=2)
second = date(year=2025, month=12, day=31)

# lasketaan aikaleimojen ero päivinä
delta = second - first
days = delta.days

#lopputulos
print(f"Päiviä jäljellä tätä vuotta: {days} kpl")

#esimerkki 2

# esim, jos lainataan kirjastosta kirja, mikä on palautus päivä
# kolmen viikon päästä
today = date.today()
today = today + timedelta(67)
print(f"palautus päivämäärä: {today}")
