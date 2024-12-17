import random

class ChessBoard:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.plansza = self._tworzenie_planszy()
        self.gonce = []
        self.generowanie_goncow(n)
        self.umieszczenie_goncow()
        self.print_plansza()

    def _tworzenie_planszy(self):
        return [[" " for _ in range(self.rozmiar)] for _ in range(self.rozmiar)]

    def print_plansza(self):
        for kolumna in range(self.rozmiar):
            print(" ---" * self.rozmiar)
            for wiersz in range(self.rozmiar):
                print(f"| {self.plansza[kolumna][wiersz]} ", end="")
            print("|")
        print(" ---" * self.rozmiar)

    def generowanie_goncow(self, n):
        pozycja = set()
        while len(pozycja) < n:
            wiersz = random.randint(0, self.rozmiar - 1)
            kolumna = random.randint(0, self.rozmiar - 1)
            pozycja.add((wiersz, kolumna))
        self.gonce = list(pozycja)

    def umieszczenie_goncow(self):
        for wiersz, kolumna in self.gonce:
            self.plansza[wiersz][kolumna] = "B"

    def szachujace_gonce(self):
        szachujace = []
        for i in range(len(self.gonce)):
            for j in range(i + 1, len(self.gonce)):
                wiersz1, kolumna1 = self.gonce[i]
                wiersz2, kolumna2 = self.gonce[j]
                if abs(wiersz1 - wiersz2) == abs(kolumna1 - kolumna2):
                    szachujace.append((self.gonce[i], self.gonce[j]))
        return szachujace

    def pokaz_gonce(self):
        return self.gonce

rozmiar = 10
n = random.randint(1, 100)

szachownica = ChessBoard(rozmiar)

print("\nPozycje gońców:")
print(szachownica.pokaz_gonce())

szachujace = szachownica.szachujace_gonce()

if len(szachujace) == 0:
    print("\nBrak gońców szachujących się.")
elif len(szachujace) == 1:
    print("\nDwa gońce szachują się wzajemnie.")
else:
    print("\nWięcej niż dwa gońce szachują się wzajemnie.")

print("\nGońce szachujące się:")
print(szachujace)