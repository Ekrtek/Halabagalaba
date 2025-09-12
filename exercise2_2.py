import math
side_a = float(input("Anna kolmion ensimmäinen kateetti:\n"))
side_b = float(input("Anna kolmion toinen kateetti:\n"))
side_c = math.sqrt(side_a ** 2 + side_b ** 2 )
side_c = round(side_c, 2)
print(f"Hypotenuusan pituus: {side_c} m")