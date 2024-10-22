x = float(input('podaj pierwsza liczbe: '))
y = float(input('podaj druga liczbe: '))

if x < 0 and y < 0:
    print("Błąd")
    exit()
if x < 0:
    x = abs(x)
if y < 0:
    y = abs(y)
if x*y == 10:
    print(f"Mnozenie {x} razy {y} daje wynik 10")
    print("Yay!")

print(f"Dodawanie {x+y}")
print(f"Odejmowanie {x-y}")
print(f"Iloraz {x/y}")
print(f"Iloczyn {x*y}")
print(f"Potega {x**2,y**2}")
print(f"Pierwiatek {x**0.5,y**0.5}")
