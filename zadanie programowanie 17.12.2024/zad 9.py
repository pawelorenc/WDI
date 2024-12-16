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

wypisz_podzialy(7)

# "/Users/pawellorenc/Documents/PyCharm/Zadania/Ćwiczenia 1/.venv/bin/python" /Users/pawellorenc/Documents/PyCharm/Zadania/Ćwiczenia 1/github/WDI/zadanie programowanie 17.12.2024/zad 9.py
# 1 + 1 + 1 + 1 + 1 + 1 + 1
# 2 + 1 + 1 + 1 + 1 + 1
# 2 + 2 + 1 + 1 + 1
# 2 + 2 + 2 + 1
# 3 + 1 + 1 + 1 + 1
# 3 + 2 + 1 + 1
# 3 + 2 + 2
# 3 + 3 + 1
# 4 + 1 + 1 + 1
# 4 + 2 + 1
# 4 + 3
# 5 + 1 + 1
# 5 + 2
# 6 + 1
# 7
#
# Process finished with exit code 0