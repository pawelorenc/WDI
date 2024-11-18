#W tym programie bedziemy uzywac wzoru Taylora
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
    with open(nazwapliku, 'w') as f:
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
    with open(nazwapliku, 'r') as f:
        for line in f:
            print(line.strip())

zapis_w_pliku("trygonometryczne.csv", katy)
odczytanie_z_pliku("trygonometryczne.csv")

