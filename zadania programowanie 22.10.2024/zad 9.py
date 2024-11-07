command = ""
saldo = 50

while True:
    command = input("Wprowadz operacje: ")
    pin = "0000"
    if command == "wplata":
        if input("Podaj pin: ") == pin:
            wplata = int(input("Jaka kwote chcesz wplacic?: "))
            saldo += wplata
            print("Co chcesz zrobic w kolejnym kroku?")
        else:
            print("Bledny pin")

    elif command == "wyplata":
        if input("Podaj pin: ") == pin:
            wyplata = int(input("Jaka kwote chcesz wplacic?: "))
            if wyplata <= saldo:
                saldo -= wyplata
                print("Co chcesz zrobic w kolejnym kroku?")
            else:
                print(f"Za malo srodkow na koncie")
                print("Co chcesz zrobic w kolejnym kroku?")
        else:
            print("Bledny pin")

    elif command == "saldo":
        if input("Podaj pin: ") == pin:
            print(f"Twoje saldo to {saldo}.")
            print("Co chcesz zrobic w kolejnym kroku?")
        else:
            print("Bledny pin")
    elif command == "koniec":
        if input("Podaj pin: ") == pin:
            quit()
    else:
        print("Nie rozumiem polecenia")
