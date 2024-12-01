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
    for wiersz, kolumna in dane:
        plansza[wiersz][kolumna] = "B"  #wstawiamy gonca na podstawie wspolrzędnych


def generowanie_goncow(rozmiar, n):#funkcja generująca losowe wspolrzędne dla goncow
    pozycja = set()  #uzywam zbioru by uniknac duplikatow
    while len(pozycja) < n:
        wiersz = random.randint(0, rozmiar - 1)
        kolumna = random.randint(0, rozmiar - 1)
        pozycja.add((wiersz, kolumna))  #dodajemy element (wiersz, kolumna) do zbioru
    return list(pozycja)  #konwertujemy zbior na liste


def szachujace_gonce(dane): #funkcja zwracajaca pozycje goncow wzajemnie się szachujacych
    szachujace = []
    for i in range(len(dane)):
        for j in range(i + 1, len(dane)):
            wiersz1, kolumna1 = dane[i]
            wiersz2, kolumna2 = dane[j]
            #sprawdzamy czy gonce szachuja się (czy sa na tej samej przekatnej)
            if abs(wiersz1 - wiersz2) == abs(kolumna1 - kolumna2):
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




