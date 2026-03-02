import math
import tkinter as tk

daten = {
    "carbon": 5730,
    "n_zero_carbon": 15.3,
    "kalium-argon": pow(1.3, 9)
}
halbwertzeit = daten.get("carbon", -1)
n_zero = daten.get("n_zero_carbon", -1)
ln2 = math.log(2)

oetzi = 53 
baer = 6.25

def berechne_n_zero(prozentsatz):
    one_percent = 15.3 / 100
    return one_percent*prozentsatz

def berechne_alter():
    fund_probe = eingabefeld.get()
    fund_probe = float(fund_probe)
    if not fund_probe or fund_probe == "":
        ausgabelabel.config(text="Bitte gib einen Wert ein.")
        return
    fund_probe = berechne_n_zero(fund_probe)
    ausgabelabel.config(text = (math.log(n_zero / fund_probe) / ln2) * halbwertzeit)

    
def erstelle_fenster():
    root = tk.Tk()
    root.geometry = ("200x300")
    root.minsize(200, 300)
    rechenfenster = tk.Frame(root)
    rechenfenster.pack()
    global ausgabelabel, eingabefeld
    ausgabelabel = tk.Label(rechenfenster, text="Alter in Jahren")
    ausgabelabel.pack()
    eingabefeld = tk.Entry(rechenfenster, width=20)
    eingabefeld.pack()
    eingabebutton = tk.Button(rechenfenster, command = lambda: berechne_alter(), text="Berechnen")
    eingabebutton.pack()
    root.mainloop()


fund_probe = berechne_n_zero(baer)
erstelle_fenster()