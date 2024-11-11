#zakladamy ze m to kolumny
#zakladamy ze n to wiersze

def intInput(a) -> int: #Funkcja na poprawny input
    while True:
        try:
            a = int(input(a))
            return a
        except ValueError:
            print("niepoprawny input!")
            continue

def wartosci_macierza(m:int, n:int, nazwa:str): #Funkcja na wpisanie wartosci do macierzy A i B
    wysokosc = [] #Ta lista laczy podgrupy(listy)
    for i in range(n):
        szerokosc = []  #Ta lista tworzy nam podgrupy(listy)
        for j in range(m):
            szerokosc.append(intInput(f"podaj wartosc punktu [{i}, {j}] {nazwa}: "))
        wysokosc.append(szerokosc)
    return wysokosc

def suma_macierzy(m1, m2):
    wynik = []
    for i in range(len(m1)):
        wiersz = []
        for j in range(len(m1[0])):
            wiersz.append(m1[i][j] + m2[i][j])
        wynik.append(wiersz)
    return wynik

def roznica_macierzy(m1, m2):
    wynik = []
    for i in range(len(m1)):
        wiersz = []
        for j in range(len(m1[0])):
            wiersz.append(m1[i][j] - m2[i][j])
        wynik.append(wiersz)
    return wynik

n = intInput("N: ")
m = intInput("M: ")

macierz1 = wartosci_macierza(m, n, "MacierzA")
macierz2 = wartosci_macierza(m, n, "MacierzB")

suma = suma_macierzy(macierz1, macierz2)
roznica = roznica_macierzy(macierz1, macierz2)

print("\nMacierz pierwszy: ")
for i in macierz1:
    print(i)

print("\nMacierz drugi: ")
for i in macierz2:
    print(i)

print("\nSuma Macierzy: ")
for i in suma:
    print(i)

print("\nRoznica Macierzy: ")
for i in roznica:
    print(i)

#Przykladowy dla malego macierza 2 na 3
# N: 2
# M: 3
# podaj wartosc punktu [0, 0] MacierzA: 2
# podaj wartosc punktu [0, 1] MacierzA: 2
# podaj wartosc punktu [0, 2] MacierzA: 2
# podaj wartosc punktu [1, 0] MacierzA: 2
# podaj wartosc punktu [1, 1] MacierzA: 2
# podaj wartosc punktu [1, 2] MacierzA: 2
# podaj wartosc punktu [0, 0] MacierzB: 2
# podaj wartosc punktu [0, 1] MacierzB: 2
# podaj wartosc punktu [0, 2] MacierzB: 2
# podaj wartosc punktu [1, 0] MacierzB: 2
# podaj wartosc punktu [1, 1] MacierzB: 2
# podaj wartosc punktu [1, 2] MacierzB: 2
#
# Macierz pierwszy:
# [2, 2, 2]
# [2, 2, 2]
#
# Macierz drugi:
# [2, 2, 2]
# [2, 2, 2]
#
# Suma Macierzy:
# [4, 4, 4]
# [4, 4, 4]
#
# Roznica Macierzy:
# [0, 0, 0]
# [0, 0, 0]

#Ta sama regula tylko wiecek klikania
# N: 3
# M: 3
# podaj wartosc punktu [0, 0] MacierzA: 1
# podaj wartosc punktu [0, 1] MacierzA: 2
# podaj wartosc punktu [0, 2] MacierzA: 4
# podaj wartosc punktu [1, 0] MacierzA: 5
# podaj wartosc punktu [1, 1] MacierzA: 1
# podaj wartosc punktu [1, 2] MacierzA: 2
# podaj wartosc punktu [2, 0] MacierzA: 3
# podaj wartosc punktu [2, 1] MacierzA: 4
# podaj wartosc punktu [2, 2] MacierzA: 1
# podaj wartosc punktu [0, 0] MacierzB: 2
# podaj wartosc punktu [0, 1] MacierzB: 3
# podaj wartosc punktu [0, 2] MacierzB: 4
# podaj wartosc punktu [1, 0] MacierzB: 1
# podaj wartosc punktu [1, 1] MacierzB: 2
# podaj wartosc punktu [1, 2] MacierzB: 3
# podaj wartosc punktu [2, 0] MacierzB: 4
# podaj wartosc punktu [2, 1] MacierzB: 1
# podaj wartosc punktu [2, 2] MacierzB: 2
#
# Macierz pierwszy:
# [1, 2, 4]
# [5, 1, 2]
# [3, 4, 1]
#
# Macierz drugi:
# [2, 3, 4]
# [1, 2, 3]
# [4, 1, 2]
#
# Suma Macierzy:
# [3, 5, 8]
# [6, 3, 5]
# [7, 5, 3]
#
# Roznica Macierzy:
# [-1, -1, 0]
# [4, -1, -1]
# [-1, 3, -1]


