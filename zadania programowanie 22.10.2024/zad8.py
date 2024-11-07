wysokosc = int(input('wysokosc choinki(nieujemna liczba): '))

print(' ' * (wysokosc-1)   + "X")

for i in range(2, wysokosc + 1):
    print(' ' * (wysokosc - i) + '*' * (2 * i - 1))

print(' ' * (wysokosc-1) + "U" )
