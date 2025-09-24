hours = input("Syötä viikon työtunnit: \n")
hours = int(hours)
hourly = input("Tuntipalkkasi: \n")
hourly = float(hourly)
if hours > 40:
    overtime = hours - 40
    hours -= overtime
    overtime_pay = overtime * (hourly * 1.5)
    pay = hours * hourly
    total_wage = pay + overtime_pay
    print(f"Viikon ansiosi ovat: {total_wage} €")
else:
    pay = hours * hourly
    print(f"Viikon ansiosi ovat: {pay} €")