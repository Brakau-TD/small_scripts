################ Taschenrechner! ################
################ Rechenzeichen:  ################
########## addieren: + ##########################
############### subtrahieren: - #################
########## multiplizieren: * ####################
############### dividieren: / ###################
## Potenz: zahl**Potenz (2**4 = zwei hoch vier ##

import sys


def addieren(zahlen):
    return int(zahlen[0])+int(zahlen[1])

def hauptprogramm():
    print("Ich bin dein Taschenrechner!")
    print("1 addieren")
    # subtrahieren
    # ...
    print("e Programm beenden")
    
    auswahl=input("Was möchtest du machen? ")
    
    if auswahl[0]=="1":
        zahlen_eingeben("+")
    elif auswahl[0]=="2":
        pass
    elif auswahl.lower()[0]=="e":
        programm_beenden()
    else:
        hauptprogramm()

def zahlen_eingeben(rechenzeichen):
    zahl=input("Gib die erste und die zweite Zahl mit einem Komma getrennt ein.")
    zahlen=zahl.split(",")
    
    if rechenzeichen=="+":
        print("Das Ergebnis ist: ",addieren(zahlen))
    elif rechenzeichen=="-":
        pass # diese Anweisung muss ersetzt werden
        
def programm_beenden():
    sys.exit()

hauptprogramm()
        