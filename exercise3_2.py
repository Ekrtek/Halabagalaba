weather = input("Syötä päivän lämpötila: \n")
weather = int(weather)
if 0 <= weather <= 10:
    print("KYLMÄÄ")
elif 11 <= weather <= 15:
    print("KOLEAA")
elif 16 <= weather <= 20:
    print("NORMAALI LÄMPÖTILA")
elif 21 <= weather <= 25:
    print("LÄMMINTÄ")
elif 26 <= weather <= 30:
    print("HELLETTÄ")