#zakladamy ze m to wiersze
#zakladamy ze n to kolumny
def intInput(a) -> int:
    while True:
        try:
            a = int(input(a))
            return a
        except ValueError:
            print("niepoprawny input!")
            continue


def rozmiar_macierza(m:int, n:int, nazwa:str):
    wysokosc = []
    for i in range(n):
        szerokosc = []
        for j in range(m):
            szerokosc.append(intInput(f"podaj wartosc punktu [{i}, {j}] {nazwa}: "))
        wysokosc.append(szerokosc)
    return wysokosc


def suma_macierzow(m1, m2):
    wynik = []
    for i in range(len(m1)):
        wiersz = []
        for j in range(len(m1[0])):
            wiersz.append(m1[i][j] + m2[i][j])
        wynik.append(wiersz)
    return wynik
def roznica_macierzow(m1, m2):
    wynik = []
    for i in range(len(m1)):
        wiersz = []
        for j in range(len(m1[0])):
            wiersz.append(m1[i][j] - m2[i][j])
        wynik.append(wiersz)
    return wynik

n = intInput("N: ")
m = intInput("M: ")

macierz1 = rozmiar_macierza(m, n, "MacierzA" )
macierz2 = rozmiar_macierza(m, n, "MacierzB" )

suma = suma_macierzow(macierz1, macierz2)
roznica = roznica_macierzow(macierz1, macierz2)

print("\nMacierz pierwszy: ")
for i in macierz1:
    print(i)

print("\nMacierz drugi: ")
for i in macierz2:
    print(i)

print("\nSuma Macierzy: ")
for i in suma:
    print(i)

print("\nRoznica Macierza: ")
for i in roznica:
    print(i)
