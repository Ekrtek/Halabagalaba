import math
side_a = float(input("Anna särmiön ensimmäisen sivun pituus:\n"))
side_b = float(input("Anna särmiön toisen sivun pituus:\n"))
side_c = float(input("Anna särmiön kolmas sivun pituus:\n"))
volume = round((side_a * side_b * side_c), 2)
print(f"Särmiön tilavuus:{volume} m3")
radius = float(input("Anna pallon säde:\n"))
ball = round(((4/3) * math.pi * radius ** 3), 2)
print(f"Pallon tilavuus:{ball} m3")