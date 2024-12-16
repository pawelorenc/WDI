def podzialy(n, maks=None):
    if maks is None:
        maks = n
    if n == 0:
        return [[]]
    wynik = []
    for i in range(1, maks + 1):
        if i <= n:
            for podzial in podzialy(n - i, i): #rekurencyjne rozbicie liczb na ich mniejsze czesci
                wynik.append([i] + podzial)
    return wynik

def wypisz_podzialy(n): #funkcja ktora pozwala nam pokazazc liste "wynik" w lepszy sposob
     podzialy_liczby = podzialy(n)
     for podzial in podzialy_liczby:
         print(" + ".join(map(str, podzial)))

wypisz_podzialy(17)

