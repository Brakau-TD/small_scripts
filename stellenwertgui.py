from tkinter import *
from stellenwertumrechner import *

class StellenwertGui:
    """
    simple Tkinter GUI
    """

    def __init__(self):
        self.create_window("Stellenwertrechner", 450, 300)
        pass

    def create_window(self, title: str, width: int, height: int):
        self._app = Tk()
        self._app.title(title)
        self._app.geometry(f"{width}x{height}")
        self._frames = self.create_frames()
        self._zahl = StringVar()
        self._gui_elements = self.gui_elements()
        self.create_gui_elements()
        self._app.mainloop()

    def create_frames(self):
        self._left_frame = Frame(self._app)
        self._left_frame.pack(side=LEFT)
        self._right_frame = Frame(self._app)
        self._right_frame.pack(side=RIGHT)

    def gui_elements(self) -> dict:
        gui_elements = {
            "Create Random ID": Label(
                self._left_frame, text="Stellenwertumrechner"
            ),
            "Info text": Label(
                self._right_frame,
                text="Gebe eine Zahl ein \nund wähle die Umrechnungsmethode.\nFalsche Eingaben werden ignoriert",
            ),
            "Output": Text(self._right_frame, width=40, height=5, pady=5, padx=15),
            "zahlenfeld": Label(self._left_frame, text="Gebe die Zahl ein."),
            "zahl": Entry(self._left_frame, textvariable=self._zahl),
            "dec zu hex": Button(self._left_frame, text="dezimal zu hexadezimal", command=lambda : self.rechne_werte_um("dezimal zu hexadezimal")),
            "dec zu dual": Button(self._left_frame, text="dezimal zu dual", command=lambda : self.rechne_werte_um("dezimal zu dual")),
            "hex zu dec": Button(self._left_frame, text="hexadezimal zu dezimal", command=lambda : self.rechne_werte_um("hexadezimal zu dezimal")),
            "hex zu dual": Button(self._left_frame, text="hexadezimal zu dual", command=lambda : self.rechne_werte_um("hexadezimal zu dual")),
            "dual zu dec": Button(self._left_frame, text="dual zu dezimal", command=lambda : self.rechne_werte_um("dual zu dezimal")),
            "dual zu hex": Button(self._left_frame, text="dual zu hexadezimal", command=lambda : self.rechne_werte_um("dual zu hexadezimal")),
        }
        return gui_elements

    def create_gui_elements(self):
        for key in self._gui_elements:
            self._gui_elements[key].pack(pady=5, padx=5, fill = X)
        self._gui_elements["Output"].insert(END, "Output: ")
        
    def check_length(self, length):
        try:
            l = int(length)
        except ValueError:
            return False
        return l

    def rechne_werte_um(self, auswahl):
        wert = self._zahl.get()
        match auswahl:
            case "dezimal zu hexadezimal":
                ergebnis = konvertiere_dec_zu_hex(wert)
            case "dezimal zu dual":
                ergebnis = konvertiere_dec_zu_dual(wert)
            case "hexadezimal zu dezimal":
                ergebnis = konvertiere_hex_zu_dec(wert)
            case "hexadezimal zu dual":
                ergebnis = konvertiere_hex_zu_dual(wert)
            case "dual zu dezimal":
                ergebnis = konvertiere_dual_zu_dec(wert)
            case "dual zu hexadezimal":
                ergebnis = konvertiere_dual_zu_hex(wert)
            case _:
                ergebnis = "Fehler"
        self._clear_gui()
        self._gui_elements["Output"].insert(END, ergebnis)
                      

    def _clear_gui(self):
        self._gui_elements["Output"].delete(0.0, END)


def main():
    gui = StellenwertGui()
    
main()