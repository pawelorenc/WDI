import random

def plansza(rozmiar): #funkcja ktora tworzy pustą szachownice
    return [[" " for _ in range(rozmiar)] for _ in range(rozmiar)]


def print_plansza(plansza):#funkcja ktora wyswietla plansze
    rozmiar = len(plansza)
    for kolumna in range(rozmiar):
        print(" ---" * rozmiar)  #stwarza pozioma linie odzielajaca wiersze
        for wiersz in range(rozmiar):
            print(f"| {plansza[kolumna][wiersz]} ", end="")  #wypisuje zawartosc planszy
        print("|")  #zamyka prawą stronę wiersza
    print(" ---" * rozmiar)  #zamyka plansze


def umieszczenie_goncow(plansza, dane): #funkcja umieszczająca gonce z tablicy 'dane' na planszy
    for row, col in dane:
        plansza[row][col] = "B"  #wstawiamy gonca na podstawie wspolrzędnych


def generowanie_goncow(size, n):#funkcja generująca losowe wspolrzędne dla goncow
    positions = set()  #uzywam zbioru by uniknac duplikatow
    while len(positions) < n:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        positions.add((row, col))  #dodajemy element (row, col) do zbioru
    return list(positions)  #konwertujemy zbior na liste


def szachujace_gonce(dane): #funkcja zwracajaca pozycje goncow wzajemnie się szachujacych
    szachujace = []
    for i in range(len(dane)):
        for j in range(i + 1, len(dane)):
            row1, col1 = dane[i]
            row2, col2 = dane[j]
            #sprawdzamy czy gonce szachuja się (czy sa na tej samej przekatnej)
            if abs(row1 - row2) == abs(col1 - col2):
                szachujace.append((dane[i], dane[j]))  #dodajemy parę gońców szachujących się
    return szachujace

rozmiar = 100  #rozmiar planszy
n = random.randint(1, 99)  #liczba gońców (N < 100)

#generowanie losowych pozycji dla gońców
dane = generowanie_goncow(rozmiar, n)

#tworzenie pustej planszy
plansza = plansza(rozmiar)

#umieszczanie gońców na planszy na podstawie tablicy 'dane'
umieszczenie_goncow(plansza, dane)

#wyświetlenie planszy
print_plansza(plansza)

#wyświetlenie pozycji gońców
print("\nPozycje gońców:")
print(dane)

# Zwrócenie pozycji gońców szachujących się
szachujace = szachujace_gonce(dane)

#zależnie od liczby szachujących się gońców, wypisujemy odpowiednią informację
if len(szachujace) == 0:
    print("\nBrak gońców szachujących się.")
elif len(szachujace) == 1:
    print("\nDwa gońce szachują się wzajemnie.")
else:
    print("\nWięcej niż dwa gońce szachują się wzajemnie.")

print("\nGońce szachujące się:")
print(szachujace)




