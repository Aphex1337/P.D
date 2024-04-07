liczba = int(input("Podaj liczbę całkowitą: "))
if liczba < 2:
    print("Podaj liczbę większą lub równą 2.")
if liczba == 0:
    print("ZERA NIE MOŻNA")
else:
    print("liczby pierwsze do", liczba, "to:", end=" ")
    for liczba in range(2, liczba + 1):
        pierwsza = True
        for i in range(2, liczba):
            if liczba % i == 0:
                pierwsza = False
                break
        if pierwsza:
            print(liczba, end=" ")