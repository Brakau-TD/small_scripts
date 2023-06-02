'''hier sind einige Übungen in Python'''
# random ist eine Bibliothek über die man Zufallszahlen generieren kann
import random 

def eins_buchstaben_raten():
    '''in dieser Übung soll ein Buchstabe geraten werden'''
    print("Buchstabenraten")
    # Buchstabenliste
    buchstaben = list("abcdefghijklmnopqrstuvwxyz")
    # Zufallszahl zwischen 0 und 25
    zufallszahl = random.randint(0,25)
    # Zufallsbuchstabe
    zufallsbuchstabe = buchstaben[zufallszahl]

    # Eingabe
    # input() nimmt eine Eingabe entgegen, die in der Variable eingabe gespeichert wird
    # dein Code hier

    # Vergleich
    # über if ... = ...: kann man etwas vergleichen
    # dein Code hier

    # Ausgabe
    # print() gibt etwas aus

def zwei_zahlen_raten():
    '''in dieser Übung sollen zwei Zahlen geraten werden'''
    print("Zahlenraten")
    # Zufallszahlen
    zahlen = [1,2,3,4,5,6,7,8,9,10]

    # Eingabe
    # dein Code hier

    # Vergleich
    # dein Code hier

    # Ausgabe
    # dein Code hier

def drei_eine_eingabe_ueberpruefen():
    '''in dieser Übung sollst du überprüfen, ob eine Eingabe eine Zahl ist'''
    print("Eingabe überprüfen")
    # Eingabe
    # mit input() kannst du eine Eingabe entgegennehmen
    # dein Code hier

    # Überprüfung
    # mit einem try: ... except: ... kannst du überprüfen, ob eine Eingabe eine Zahl ist
    # falls die Eingabe keine Zahl ist, wird der Code im except-Block ausgeführt
    # du findest eine Erläuterung hier: https://www.w3schools.com/python/python_try_except.asp

def vier_eine_einkaufsliste_anlegen():
    '''in dieser Übung sollst du eine Einkaufsliste anlegen. Dafür benutzen wir eine Liste'''
    print("Einkaufsliste anlegen")
    # Informationen zu while-Schleifen findest du hier: https://www.w3schools.com/python/python_while_loops.asp

    # Einkaufsliste wird leer angelegt
    einkaufsliste = []

    # Eingabe
    # mit while <bedingung>: kannst du eine Schleife erstellen, die solange ausgeführt wird, bis die Bedingung nicht mehr erfüllt ist
    # die Bedingung kann sein, dass die Variable "sache" nicht leer ist, also sache != ""
    # mit input kannst du eine Eingabe entgegennehmen
    # mit .append() kannst du ein Element an eine Liste anhängen
    # dein Code hier

    # Ausgabe
    # mit print() kannst du etwas ausgeben
    # dein Code hier

def fuenf_elemente_aus_einer_liste_entfernen():
    '''in dieser Übung sollst du Elemente aus einer Liste entfernen'''
    print("Elemente aus einer Liste entfernen")
    # Informationen zu for-loops findest du hier: https://www.w3schools.com/python/python_for_loops.asp
    liste = ["papier", "stift", "radiergummi", "lineal", "schere", "kleber", "farbe", "pinsel"]

    # Abfrage
    # mit for <element> in <liste>: kannst du über eine Liste iterieren
    # mit print() kannst du etwas ausgeben
    # mit input() kannst du eine Eingabe entgegennehmen
    # mit if <bedingung>: kannst du eine Bedingung formulieren
    # mit .remove() kannst du ein Element aus einer Liste entfernen
    # dein Code hier

    # Ausgabe
    # mit print() kannst du etwas ausgeben
    # dein Code hier

def sechs_sudoku_zeile_erstellen():
    '''in dieser Übung sollst du eine einzelne Zeile für Sudoku erstellen'''
    # Informationen zu random findest du hier: https://www.w3schools.com/python/module_random.asp
    # eine Sudoku-Zeile enhält alle Zahlen von 1 bis 9. Die letzte Zahl in range(1,10) wird nicht mitgezählt
    zahlen = list(range(1, 10))
    # benutze .shuffle(), um die Zahlen in der Liste zahlen zu mischen
    # Informationen zu .shuffle() findest du hier: https://www.w3schools.com/python/ref_random_shuffle.asp
    # dein Code hier

    # Ausgabe
    # mit print() kannst du etwas ausgeben
    # dein Code hier
    return zahlen

def sieben_listen_von_listen_vergleichen():
    '''in dieser Übung sollst du zwei Listen vergleichen'''
    # Informationen zu Listen von Listen findest du hier: https://www.w3schools.com/python/python_lists.asp
    # in den folgenden zwei Listen sind die Zahlen 4 und 9 an der jeweiligen Stelle gleich
    zeile_eins = [1,2,3,4,5,6,7,8,9]
    zeile_zwei = [3,6,5,4,7,8,2,1,9]
    # schreibe den Code, um die Listen zu vergleichen. Zähle in einem for-loop von 1 bis len(zeile_eins)...
    # und vergleiche die Elemente an der jeweiligen Stelle in zeile_zwei
    # Wenn die Zahlen sich unterscheiden gib "Unterschied" aus, wenn sie gleich sind gib "Gleich" aus

def acht_elemente_in_einer_liste_vertauschen():
    '''in dieser Übung sollst du Elemente in einer Liste vertauschen'''
    zeile_eins = [1,2,3,4,5,6,7,8,9]
    zeile_zwei = [3,6,5,4,7,8,2,1,9]
    # schreibe den Code, um die Elemente in den Listen zu vergleichen. Zähle in einem for-loop von 1 bis len(zeile_eins)...
    # und vergleiche die Elemente an der jeweiligen Stelle in zeile_zwei
    # wenn die Zahlen gleich sind, dann hole und entferne die Zahl in zeile_zwei mit z = zeile_zwei.pop(position)
    # Informationen zu Listenoperationen findest du hier: https://www.w3schools.com/python/python_lists_methods.asp
    # und füge sie mit .append() an zeile_zwei wieder an.
    # dein Code hier

    # Ausgabe
    # dein Code hier

def neun_weitere_sudoku_zeilen_erstellen():
    '''in dieser Übung sollst du eine Zeile (aus drei Feldern) für Sudoku erstellen'''
    sudoku_spielfeld = []
    # schreibe einen for-loop in range(9) und füge die Zeilen zu der Liste hinzu
    # du bekommst die Zeilen aus der Übung sechs
    # dein Code hier



def beispielcode_uebung_sechs():
    '''hier ist ein Beispielcode für eine Liste von Listen zu Übung 6'''
    meine_liste = []
    innere_list = []

    for i in range(3):
        innere_list = []
        for j in range(3):
            innere_list.append(j)
        meine_liste.append(innere_list)
    print(meine_liste)

def hauptmenue():
    funktionen = {
        "1": eins_buchstaben_raten,
        "2": zwei_zahlen_raten,
        "3": drei_eine_eingabe_ueberpruefen,
        "4": vier_eine_einkaufsliste_anlegen,
        "5": fuenf_elemente_aus_einer_liste_entfernen,
        "6": sechs_sudoku_zeile_erstellen,
        "7": sieben_listen_von_listen_vergleichen,
        "8": acht_elemente_in_einer_liste_vertauschen,
        "9": neun_weitere_sudoku_zeilen_erstellen,
    }
    print("Willkommen zu den Übungen in Python")
    print("Bitte wähle eine Übung aus:")
    for key, value in funktionen.items():
        print(f'{key}: {value.__doc__}')

    auswahl = input("Auswahl: ")

    try:
        funktionen[auswahl]()
    except KeyError:
        print("Bitte wähle eine Zahl zwischen 1 und 9")
        hauptmenue()

hauptmenue()
