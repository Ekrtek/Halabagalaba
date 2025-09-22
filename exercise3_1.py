number1 = int(input("Anna ensimmäinen luku: \n"))
number2 = int(input("Anna toinen luku: \n"))
if number1 > number2:
    print(f"Suurempi luku = {number1}")
elif number2 > number1:
    print(f"Suurempi luku = {number2}")
else:
    print("Numerot ovat yhtä suuria.")