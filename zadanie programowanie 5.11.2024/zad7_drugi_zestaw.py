#Zadanie 7 - Napisz program, ktory oblicza wartosc N! dla N w zakresie od 1 do M, gdzie M jest wartoscia podana przez uzytkownika.

def liczba(a) -> int:
    while True:
        try:
            k = int(input(a))
            if k < 1 or k > 1000000:
                print("Podana zla wartosc!")
                continue
            return k
        except ValueError:
            print("Podana zla wartosc, podaj liczbe calkowita!")

def silnia(n: int):
    suma = 1
    for i in range(1, n + 1):
        suma *= i
        roznica = int(suma / i)
        print(suma)
        print(f"Roznica wyniku to {suma}-{roznica}={suma-roznica}!")

m = liczba("Podaj liczbe: ")
silnia(m)




