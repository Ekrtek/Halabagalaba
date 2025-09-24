number1 = input("Anna ensimmäinen luku: \n")
number1 = int(number1)
number2 = input("Anna toinen luku: \n")
number2 = int(number2)

if number1 > number2:
    print(f"Suurempi luku = {number1}")
elif number2 > number1:
    print(f"Suurempi luku = {number2}")
else:
    print("Numerot ovat yhtä suuria.")