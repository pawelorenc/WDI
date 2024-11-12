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
    for i in range(1,int(liczba**1/2)+1, 2):
        if liczba % i == 0:
            print("liczba nie jest pierwsza")
            break
    else:
        print("liczba pierwsza")

