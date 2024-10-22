def liczb(a) -> int:
    while True:
        try:
            n = int(input(a))
            break
        except ValueError:
            print("Nieprawidlowy input. Podaj ponownie liczbe.")
    return n

liczba = liczb(("Podaj liczbe: "))

if liczba <= 2:
    print("Liczba nie jest pierwsza.")
else:
    for i in range(2,int(liczba)):
        if liczba % i == 0:
            print("liczba nie jest pierwsza")
            break
    else:
        print("liczba pierwsza")

