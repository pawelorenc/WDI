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

n = liczba("Podaj liczbe: ")
silnia(n)




