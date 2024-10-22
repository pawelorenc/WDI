liczba1 = int(input("Podaj pierwsza liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))

while True:
    pytanie = input("Czy chcesz wprowadzic nowe dane?: ")
    if pytanie.upper() == ("N"):
        print("Działanie na tych samych liczbach")
    elif pytanie.upper() == ("T"):
        liczba1 = int(input("Podaj pierwsza liczbe: " ))
        liczba2 = int(input("Podaj druga liczbe: " ))

    else:
        print("Niepoprawna komenda.")
        False
    def runMatch():
        znak = input("Podaj znak: ")
        command = True
        match znak:
            case "+":
                print(liczba1 + liczba2)
            case "-":
                print(liczba1 - liczba2)
            case "*":
                print(liczba1 * liczba2)
            case "/":
                print(liczba1 / liczba2)
            case "#":
                print(liczba1 ** liczba2)
            case "^":
                print(liczba1 ** (1/liczba2))
            case "" :
                print("Zla komenda!")
            case "stop":
                print("Stop programu.")
                exit()
    runMatch()
