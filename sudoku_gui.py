from tkinter import *
from sudoku import *

class SudokuGui:
    """
    simple Tkinter GUI
    """

    def __init__(self):
        self.create_window("Sudoku!", 750, 300)
        pass

    def create_window(self, title: str, width: int, height: int):
        self._app = Tk()
        self._app.title(title)
        self._app.geometry(f"{width}x{height}")
        self._frames = self.create_frames()
        self._schwierigkeit = StringVar()
        self._gui_elements = self.gui_elements()
        self.create_gui_elements()
        self._app.mainloop()

    def create_frames(self):
        self._left_frame = Frame(self._app)
        self._left_frame.pack(side=LEFT)
        self._right_frame = Frame(self._app)
        self._right_frame.pack(side=RIGHT, padx=10)

    def gui_elements(self) -> dict:
        gui_elements = {
            "Sudoku": Label(
                self._left_frame, text="Sudoku"
            ),
            "Info text": Label(
                self._left_frame,
                text="Fülle deine Zahl aus und clicke auf übernehmen.",
            ),
            "Schwierigkeitsgrad": Label(self._left_frame, text="Gebe einen Schwierigkeitsgrad zwischen 1 und 10 ein.\n1 ist leicht, 10 schwer."),
            "Schwierigkeits": Entry(self._left_frame, textvariable=self._schwierigkeit),
            "abschicken": Button(self._left_frame, text="abschicken", command=lambda : self.menue("abschicken")),
            "überprüfen": Button(self._left_frame, text="ueberpruefen", command=lambda : self.menue("überprüfen")),
            "Name": Button(self._left_frame, text="name", command=lambda : self.menue("name")),
        }
        return gui_elements


    def create_entry_fields(self):
        '''
        creates a 9x9 array of entry fields, 
        each field is one character wide
        it will be the sudoku board
        '''
        self._entry_fields = []
        self._entry_temp = []
        self._text_variables = []
        self._line_temp =[]
        for i in range(9):
            for j in range(9):
                self._entry_temp.append(StringVar())
                self._line_temp.append(Entry(self._right_frame, width=3, textvariable=self._entry_temp[-1]))
            self._entry_fields.append(self._line_temp)
            self._line_temp = []
            self._text_variables.append(self._entry_temp)
            self._entry_temp = []
        return self._entry_fields

    def create_gui_elements(self):
        for key in self._gui_elements:
            self._gui_elements[key].pack(pady=5, padx=5, fill = X)
        
    def check_length(self, length):
        try:
            l = int(length)
        except ValueError:
            return False
        return l

    def menue(self, auswahl):
        wert = self._schwierigkeit.get()
        match auswahl:
            case "abschicken":
                if self.check_length(wert):
                    self._clear_gui()
                    self._sudoku = CreateInitialBoard(wert)
                    self.create_entry_fields()
                    for i in range(9):
                        for j in range(9):
                            self._entry_fields[i][j].grid(row=i, column=j, padx = 5, pady = 5)
        self._clear_gui()
                      

    def _clear_gui(self):
        '''this function will be assigned to the clear button'''
        return


def main():
    gui = SudokuGui()
    
main()