""" ein kleines Vokabelprogramm """
import sys
import csv
import os


vokabeldict = {}


def vokabeln_hinzufuegen():
    condition = True
    print("Gebe Vokabeln ein oder drücke [enter] zum Beenden")
    print("Gebe doppelte Begriffe auf Englisch mit einem Komma getrennt ein.\n")
    while condition:
        de = input("deutsches Wort: ")
        if de == "":
            break
        eng = input("englisches Wort: ")
        englist = eng.split(",")
        vokabeldict[de] = englist


def vokabeln_abfragen():
    deutsche_worte = list(vokabeldict.keys())
    richtige_worte = 0
    for i, key in enumerate(vokabeldict):
        alter_wert = richtige_worte
        print(f"Was heißt {key} auf Englisch? ", end="")
        antwort = input("")
        for vals in vokabeldict[key]:
            richtige_worte += 1 if antwort == vals else 0
        print("Richtig") if richtige_worte > alter_wert else print("Falsch :( ")
    print(f"Du hast {richtige_worte} von {len(vokabeldict.keys())} gewusst!")
    input("Press enter to continue")


def vokabeln_speichern():
    save = dictionary_zu_liste([])
    with open("vokabelliste1.csv", "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(save)
    print("Gespeichert!")


def dictionary_zu_liste(new_list):
    for key, val in vokabeldict.items():
        new_list.append([key, *val])
    return new_list


def vokabeln_laden():
    """Hier wird eine Vokabelliste aus einer csv-Datei geladen"""
    listenzeilen = []
    with open("vokabelliste.csv", mode="r", encoding="utf-8-sig") as vokabelliste:
        vokabeln = [item for item in csv.reader(vokabelliste, delimiter=";")]
    for line in vokabeln:
        a = line.pop(0)
        vokabeldict[a] = line
    print("Geladen!")


def menu():
    """Hier soll der/die NutzerIn auswählen, was er/sie im Programm machen will"""
    for i, val in enumerate(funcs.keys()):
        print(f"[{i}] {val}") if i > 0 else None
    print("Bitte wähle eine Zahl aus. ", end="")
    antwort = input()
    clear = lambda: os.system("cls")
    clear()
    if antwort.isdigit():
        funcs[list(funcs)[int(antwort)]]()
    menu()


def beenden():
    sys.exit()


funcs = {
    "Menü": menu,
    "abfragen": vokabeln_abfragen,
    "eingeben": vokabeln_hinzufuegen,
    "speichern": vokabeln_speichern,
    "laden": vokabeln_laden,
    "beenden": beenden,
}


funcs["Menü"]()
