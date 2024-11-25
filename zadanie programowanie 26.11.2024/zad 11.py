#W tym programie bedziemy uzywac wzoru na szereg Taylora
#Poniewaz nie uzywamy biblioteki math musze recznie wpisac wartosc PI


def silnia(n):
    if n == 0 or n == 1:
        return 1
    suma = 1
    for i in range(2, n+1):
        suma *= i
    return suma

def sin(x, dokladnosc=85): #Szereg Taylora do funkcji sin.
    suma = 0
    for i in range(dokladnosc):
        znak = (-1) ** i
        suma += znak * (x** (2 * i + 1)) / silnia(2 * i +1)
    return suma

def cos(x, dokladnosc=85): #Szereg Taylora do funkcji cos.
    suma = 0
    for i in range(dokladnosc):
        znak = (-1) ** i
        suma += znak * (x ** (2 * i)) / silnia(2 * i)
    return suma

def tg(x):
    #tg(x)=sin(x)/cos(x)
    cos_x = cos(x)
    sin_x = sin(x)
    if cos_x == 0:
        return float('inf')
    tg_x = sin_x/cos_x
    return tg_x

def ctg(x):
    tg_x = tg(x)
    if tg_x == 0:
        return float('inf')
    ctg_x = 1/tg_x
    return ctg_x

PI = 3.141592653589793 #Uzywamy wpisanej wartosci dla PI ze wzgledu na brak mozliwosci zaimplementowania biblioteki math.

katy = [0, PI/6, PI/4, PI/3, PI/2, PI, 2*PI] #Radianowe wartosci dla podanych katow w zadaniu.

def zapis_w_pliku(nazwapliku, katy):
    with open(nazwapliku, 'w') as f: #otwiera plik w trybie zapisu
        f.write(f'Kąt(radiany) z sin(x), cos(x), tg(x), ctg(x)\n')
        for kat in katy:
            f.write(f'\nKąt: {kat} radianow\n')
            sin_x = sin(kat)
            cos_x = cos(kat)
            tg_x = tg(kat)
            ctg_x = ctg(kat)
            f.write(f'sin(x) = {sin_x}\n')
            f.write(f'cos(x) = {cos_x}\n')
            f.write(f'tg(x) = {tg_x}\n')
            f.write(f'ctg(x) = {ctg_x}\n')


def odczytanie_z_pliku(nazwapliku):
    with open(nazwapliku, 'r') as f: #otwiera plik w trybie odczytu
        for line in f:
            print(line.strip()) #strip usuwa zbedne znaki przed  i po zawartoscia tekstowa jak spacja

zapis_w_pliku("wartosci.csv", katy)
odczytanie_z_pliku("wartosci.csv")

#Wynik kodu zapisany do pliku wartosci.csv
# Kąt(radiany) z sin(x), cos(x), tg(x), ctg(x)
#
# Kąt: 0 radianow
# sin(x) = 0.0
# cos(x) = 1.0
# tg(x) = 0.0
# ctg(x) = inf
#
# Kąt: 0.5235987755982988 radianow
# sin(x) = 0.49999999999999994
# cos(x) = 0.8660254037844386
# tg(x) = 0.5773502691896257
# ctg(x) = 1.7320508075688774
#
# Kąt: 0.7853981633974483 radianow
# sin(x) = 0.7071067811865475
# cos(x) = 0.7071067811865475
# tg(x) = 1.0
# ctg(x) = 1.0
#
# Kąt: 1.0471975511965976 radianow
# sin(x) = 0.8660254037844385
# cos(x) = 0.5000000000000001
# tg(x) = 1.7320508075688765
# ctg(x) = 0.5773502691896261
#
# Kąt: 1.5707963267948966 radianow
# sin(x) = 1.0000000000000002
# cos(x) = 4.2539467343847745e-17
# tg(x) = 2.3507581604559628e+16
# ctg(x) = 4.253946734384773e-17
#
# Kąt: 3.141592653589793 radianow
# sin(x) = 3.3280566969799443e-16
# cos(x) = -1.0000000000000002
# tg(x) = -3.328056696979944e-16
# ctg(x) = -3004756502217806.0
#
# Kąt: 6.283185307179586 radianow
# sin(x) = 3.300904356666342e-15
# cos(x) = 0.9999999999999902
# tg(x) = 3.3009043566663745e-15
# ctg(x) = 302947281092964.7
#
# Process finished with exit code 0
