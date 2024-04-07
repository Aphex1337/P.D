miesiac = int(input("Podaj numer miesiąca (od 1 do 12): "))
dzien = int(input("Podaj numer dnia: "))
rok = int(input("Podaj rok: "))
dni_w_miesiacu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if miesiac < 1 or miesiac > 12:
    print("Podaj poprawny numer miesiąca (od 1 do 12).")
elif dzien < 1 or dzien > dni_w_miesiacu[miesiac - 1]:
    print("Podaj poprawny numer dnia dla wybranego miesiąca.")
if rok < 1900:
    print("Podaj rok powyżej 1900")
else:
    print("Daty danego miesiąca:")
    for d in range(1, dni_w_miesiacu[miesiac - 1] + 1):
        if d == dzien:
            print("Wybrana przez ciebie")
        else:
            print(f"2024/{miesiac}/{d}")