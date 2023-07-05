import tkinter as tk
from fileoperations import FileOperations
from structureoperations import StructureOperations

class AppGui:
    """
    Graphische Oberfläche für alles mögliche
    
    """

    def __init__(self, hauptprogramm):
        """
        das Hauptprogramm wird hier in die __init__ übergeben.
        das bedeutet, dass man über self.hp. auf die Methoden im Hauptprogramm zugreifen kann
        zuerst werden ein paar Variablen angelegt
        """
        self.listboxvariable = None
        self.radiobuttons = None
        self.radb2 = None
        self.radb1 = None
        self._right_frame = None
        self.radio = None
        self._left_frame = None
        self.hp = hauptprogramm
        self._text_variables: list = []
        self._listvariables: list = []

        self._information: dict = {
            "appname": "My App",
            "title": "My App",
            "description": "This is my app. It does something.",
            "width": 480,
            "height": 600,
            "padx": 10,
            "pady": 10,
        }
        self.variable_dictionary = {
            "text_variables": [self._text_variables, 4],
            "listvariables": [self._listvariables, 4],
        }
        self.items = []

        self.create_window()

    def initialize_variables(self):
        """hier werden Variablen in Listen angelegt. Alle Variablen hier nehmen Strings auf"""
        for element in self.variable_dictionary:
            for _ in range(self.variable_dictionary[element][1]):
                self.variable_dictionary[element][0].append(tk.StringVar())

    def initialize_dictionary(self) -> dict:
        """
        in diesem Dictionary gui_elements werden alle Elemente der Benutzeroberfläche angelegt.
        Label sind Textelemente, die z.B. einen erklärenden Text enhalten
        Button sind das, was man sich drunter vorstellt. Drauf klicken und etwas passiert.
            die Buttons sind immer auch an ein command geknüpft. D.h. mit einem Button wird eine Funktion aufgerufen
        Entry sind Eingabefelder. Diese müssen eine Variable haben, damit man die Eingaben auslesen kann.
        Text sind Textfelder für mehrzeilige Texte
        Listbox nehmen Texte zeilenweise auf. Das heißt, dass der Anwender auf eine Zeile klicken kann und die
            listbox gibt den Wert der Zeile zurück (z.B. Dateien in einem Verzeichnis)
        Radiobutton sind anklickbare Felder. Mehrere Buttons können sich eine Variable teilen. So weiß der Programmierer
            dann welcher Button geklickt wurde.
        """
        self.radio = tk.IntVar()
        self.radio.set(1)
        self._toplabel = tk.StringVar(value = "Top-Label")
        self._rightlabel = tk.StringVar(value = "Right-Label")
        gui_elements = {
            "Labels": {
                "L1": tk.Label(
                    self._top_frame, justify="left",
                    textvariable = self._toplabel
                ),
                "L2": tk.Label(
                    self._left_frame, text="Left-Frame description", justify="left"
                ),
                "L3": tk.Label(
                    self._right_frame, textvariable=self._rightlabel, justify="right"
                ),
                "L4": tk.Label(
                    self._bottom_frame, text="Bottom-Frame description", justify="right"
                ),
            },
            "Buttons": {
                "B1": tk.Button(
                    self._left_frame,
                    text="Button 1",
                    command=lambda: self.menu("button1"),
                    justify="left",
                ),
                "B2": tk.Button(
                    self._left_frame,
                    text="abschicken",
                    command=lambda: self.menu("button2"),
                    justify="left",
                ),
            },
            "Entries": {
                "E1": tk.Entry(self._left_frame, textvariable=self._text_variables[0],),
                "E2": tk.Entry(self._left_frame, textvariable=self._text_variables[1]),
            },
            "Text": {
                "T1": tk.Text(
                    self._left_frame,
                    height=5,
                    width=30,
                    wrap="word",
                    state="normal",
                    bg="DarkOliveGreen1"
                ),
                "T2": tk.Text(
                    self._right_frame,
                    height=5,
                    width=22,
                    wrap="word",
                    state="normal",
                    bg="lightblue",
                ),
            },
            "Listboxes": {
                "L": tk.Listbox(
                    self._right_frame,
                    listvariable=self.listboxvariable,
                    height=20,
                    width=30,
                    selectmode="single",
                    bg="gold"
                ),
            }, }
        self.radiobuttons = {
            "R1": tk.Radiobutton(
                self._left_frame,
                text="Radiobutton 1",
                variable=self.radio,
                value=1),
            "R2": tk.Radiobutton(self._left_frame,
                                 text="Radiobutton 1",
                                 variable=self.radio,
                                 value=1)
        }
        return gui_elements

    def create_window(self):
        '''
        Hier wird das Programmfenster "gebaut"
        '''
        self._app = tk.Tk()
        title = self._information["appname"]
        self._app.title(title)
        self._app.geometry(
            f'{self._information["width"]}x{self._information["height"]}'
        )
        self.listboxvariable = tk.StringVar(value=self.items)

        self.create_frames()
        self.create_gui_elements()
        self._clear_gui()

        self._app.mainloop()  # Hier beginnt das Programm

    def create_frames(self):
        '''
        Diese Benutzeroberfläche hat vier Frames. Frames machen es leichter, die
        Benutzeroberfläche zu strukturieren. Man kann also leichter z.B. einen Button
        auf ein bestimmtes Viertel der Oberfläche setzen
        '''
        self._left_frame = tk.Frame(self._app, height=10, width=50)
        self._left_frame.grid(row=1, column=0, sticky="w")
        self._right_frame = tk.Frame(self._app, height=10, width=50)
        self._right_frame.grid(row=1, column=1, sticky="e")
        self._top_frame = tk.Frame(self._app, height=10, width=100)
        self._top_frame.grid(row=0, column=0, sticky="n")
        self._bottom_frame = tk.Frame(self._app, height=10, width=100)
        self._bottom_frame.grid(row=2, column=0, sticky="s")

    def create_gui_elements(self):
        """Hier werden aus dem Dictionary alle Elemente der Benutzeroberfläche erstellt"""
        self.initialize_variables()
        self._gui_elements = self.initialize_dictionary()
        dictkeys = list(self._gui_elements.keys())
        self._create_gui(dictkeys)

    def _create_gui(self, dictkeys):
        """und hier werden sie alle 'gezeichnet'"""
        self.all_elements = {}

        for key in dictkeys:
            for element in self._gui_elements[key]:
                self._gui_elements[key][element].pack(
                    pady=self._information["pady"],
                    padx=self._information["padx"],
                    side="top",
                    anchor="w",
                )
                self.all_elements[element] = self._gui_elements[key][element]
        self.all_elements["E1"].insert(0, "enter base folder")

        for key, value in self.radiobuttons.items():
            print(key,value)
            value.pack(
                pady=self._information["pady"],
                padx=self._information["padx"],
                side="top",
                anchor="w",
            )
            self.all_elements[key] = value

        self.all_elements["L"].bind("<<ListboxSelect>>", self.onselect)
        #self.all_elements["L3"]

    def onselect(self, event):
        print("onselect")
        self._rightlabel.set(self.allcontent[
            self.all_elements["L"].curselection()[0]]
        )

    def menu(self, choice: str):
        """
        diese Methode verzweigt je nach Button der gedrückt wurde
        schaue mal ins Dictionary oben, da siehst du, wie man hierhin kommt
        """
        # die Befehle match... choice... gibt es erst seit Python 3.10 
        match choice:
            case "button1":
                self.app_function_one()
            case "button2":
                self.app_function_two()

    def _clear_gui(self, gui_element=["alle"]):
        """
        Manchmal muss man die ganze Oberfläche auch mal leer machen
        manchmal reicht es aber auch nur Teile zu leeren, dafür kann man
        eine Liste an diese Methode hier übergeben, um nur Teilbereiche zu säubern.
        Z.B. ["Text","Entries"]
        wenn man nicht an diese Methode übergibt, werden automatisch alle Elemente geleert
        """
        to_clean = ["Text", "Listboxes", "Entries", "Radiobuttons"]

        if gui_element == ["alle"]:
            to_clean = to_clean
        else:
            to_clean = gui_element

        for element in to_clean:
            match element:
                case "Text":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].delete(1.0, "end")
                case "Listboxes":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].delete(0, "end")
                case "Entries":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].delete(0, "end")

    def app_function_one(self):
        """
        Diese Methode wird vom Button 1 angesteuert.
        Hier liest sie das erste Entry-Feld aus
        """
        self._clear_gui(["Text"])
        self.all_elements["T1"].insert("end", self._text_variables[0].get())
        self.allcontent = self.hp.get_folders(self._text_variables[0].get())
        print(self.allcontent)
        self._clear_gui(["Listboxes"])
        self.listboxvariable.set(self.allcontent)

        #self.all_elements["L3"].insert("end", dircontent)

    def app_function_two(self):
        """
        Diese Methode wird vom Button 2 angesteuert.
        Sie liest das zweite Entry-Feld aus und ruft dann,
        je nachdem, welcher Radiobutton angeklickt ist,
        welche Methode im Hauptprogramm angesteuert wird.
        das Resultat wird hier in der Variable antwort gespeichert.
        """
        radiobuttonvalue = self.get_value()
        self._clear_gui(["Text"])
        match radiobuttonvalue:
            case 0:
                pass
            case 1:
                self.all_elements["T2"].insert("end", f'Du hast den Radiobutton {radiobuttonvalue} gewählt')
                antwort = self.hp.berechne_etwas(self._text_variables[0].get())
            case 2:
                self.all_elements["T2"].insert("end", f'Du hast den Radiobutton {radiobuttonvalue} gewählt')
                antwort = self.hp.sortiere_etwas(self._textvariables[1].get())

    def get_value(self):
        """Liest aus, welcher Radiobutton angeklickt wurde"""
        value = self.radio.get()
        if value != "":
            return value
        else:
            return 0

fo = FileOperations()
so = StructureOperations(fo)
ag = AppGui(so)
