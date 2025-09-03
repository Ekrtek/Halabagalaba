# perus importilla nämä olisi hassu:
# import datetime
# today = datetime.datetime.now()
from datetime import datetime

today = datetime.today()
month = datetime.today().month
print(f"{today.month:02d}")
print(today)


# jos haluaa saada päivä ja kuun kahen numeron formattiin f stringissä {month:02d} tai {day:02d}