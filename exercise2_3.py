palkka = float(input("Anna kuukausipalkka: \n"))
vero = float(input("Anna veroprosentti: \n"))
veroprosentti = vero / 100
tax_amount = palkka * veroprosentti
remainder = palkka - tax_amount
print(f"Käteenjäävä osuus: {remainder} €")
print(f"Verot: {tax_amount} €")