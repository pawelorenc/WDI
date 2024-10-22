number1 = int(input("podaj liczbe pierwsza: "))
number2 = int(input("podaj liczbe druga: "))

liczby = list(range(number1, number2 + 1))

srednia = sum(liczby) / len(liczby)

if len(liczby) <= 20:
    for liczby1 in liczby:
        print(liczby1)

else:
    numbers_sorted_by_distance = sorted(liczby , key=lambda x: abs(x-srednia))

    closest_to_average = numbers_sorted_by_distance[0]
    numbers_sorted_by_distance.remove(closest_to_average)

    closest_6 = numbers_sorted_by_distance[:6]

    for liczby1 in closest_6:
        print(liczby1)

