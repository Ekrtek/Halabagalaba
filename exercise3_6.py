year = input("Year: \n")
year = int(year)
karkausvuosi = False
if year  % 400 == 0:
    karkausvuosi = True
elif year % 100 == 0:
    karkausvuosi = False
elif year % 4 == 0:
    karkausvuosi = True

if karkausvuosi:
    print("Karkausvuosi: KYLLÄ")
else:
    print("Karkausvuosi: EI")
