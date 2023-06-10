# Drevers großartiges Partyspiel
import sys


def suchroutine1(zahl, bereich):
    testzahl, counter = 0, 0
    while testzahl != zahl and counter < bereich+1:
        print(testzahl, ",", end="")
        testzahl += 1
        counter += 1
    if testzahl == zahl:
        print("\nIch habe "+str(counter)+" Versuche gebraucht.", end="")
        ergebnisliste_suchroutine1.append(counter)
    else:
        print("\nHmmpf! Irgendwer hat geschummelt. Ich war's nicht!")
    print(ergebnisliste_suchroutine1)
    main()


def suchroutine2(zahl, bereich):
    testzahl, counter, untere_grenze = 0, 0, 0
    obere_grenze = bereich

    while testzahl != zahl:
        if testzahl < zahl:

            untere_grenze = testzahl
            testzahl = ganze_zahl(obere_grenze/2)+untere_grenze
            temp = untere_grenze + \
                ganze_zahl((obere_grenze-untere_grenze)/2)
            obere_grenze = temp

        elif testzahl > zahl:

            obere_grenze = testzahl
            temp = ganze_zahl((obere_grenze-untere_grenze)/2)
            testzahl = untere_grenze+temp

        counter += 1
        if counter == 1000:
            break
    print("Testzahl ist: ", testzahl)
    ergebnisliste_suchroutine2.append(counter)
    main()


def ganze_zahl(zahl):
    # spaltet Nachkommastellen ab ohne zu runden
    return (int((str(zahl).split('.')[0])))


ergebnisliste_suchroutine1 = []
ergebnisliste_suchroutine2 = []


def main():

    print("Normale Suche: ", ergebnisliste_suchroutine1)
    print("Coole Suche: ", ergebnisliste_suchroutine2)

    version = input("Suchroutine 1 oder 2? ")
    if int(version) >= 3:
        sys.exit()
    elif int(version) == 1:
        zahl, bereich = input(
            "Geben Sie eine Zahl ein und einen Bereich mit einem Komma getrennt ein: ").split(",")
        try:
            suchroutine1(int(zahl), int(bereich))
        except ValueError:
            print("Nö")
    elif int(version) == 2:
        zahl, bereich = input(
            "Geben Sie eine Zahl ein und einen Bereich mit einem Komma getrennt ein: ").split(",")
        try:
            suchroutine2(int(zahl), int(bereich))
        except ValueError:
            print("Nope!")


main()
