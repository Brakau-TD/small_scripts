'''
Hier ist das Hauptprogramm der App
Es besteht aus einer Klasse mit drei Methoden.
Die machen noch nix großes, aber das kann ja noch werden.
Der Benutzer startet über das File 'myapp_gui. Dieses File
importiert die Klasse MyApp von hier.

Die Programmideen muss man selber mitbringen.
Aber das Internet ist voll von 'app ideas for python'
z.B. hier:
https://www.freecodecamp.org/news/python-projects-for-beginners/
'''


class MyApp:
    def __init__(self):
        self.variable_one = ""
        self.variable_two = 0
        
    def suche_etwas(self, text):
        print(f"Hier würde das Programm etwas mit {text} machen und eventuell etwas zurückgeben.")
    
    def berechne_etwas(self, text):
        print(f"Hier würde das Programm etwas mit {text} machen und eventuell etwas zurückgeben.")
        self.variable_one = text
        return "Hallo"
    
    def sortiere_etwas(self,text):
        print(f"Hier würde das Programm etwas mit {text} machen und eventuell etwas zurückgeben.")
        return "Huhu"
        