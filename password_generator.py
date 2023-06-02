import random
import string
from tkinter import *

characterlist = list("!'§$%&()=?_-+#*;:")
def create_random_id(length: int) -> str:
    """creates a random string"""
    _random_id = ""
    for _ in range(length):
        _random_id += _random_id.join(
            random.choice(random.choice([string.ascii_letters, string.digits, characterlist]))
        ) 
    return _random_id


class RandomGui:
    """
    simple Tkinter GUI
    """

    def __init__(self):
        self.create_window("create password", 400, 200)
        pass

    def create_window(self, title: str, width: int, height: int):
        self._app = Tk()
        self._app.title(title)
        self._app.geometry(f"{width}x{height}")
        self._frames = self.create_frames()
        self._length = StringVar()
        self._gui_elements = self.gui_elements()
        self.create_gui_elements()
        photo = PhotoImage(file = "iconpass.png")
        self._app.iconphoto(False, photo)
        self._app.mainloop()

    def create_frames(self) -> dict:
        self._left_frame = Frame(self._app)
        self._left_frame.pack(side=LEFT)
        self._right_frame = Frame(self._app)
        self._right_frame.pack(side=RIGHT)

    def gui_elements(self) -> dict:
        gui_elements = {
            "Create Random ID": Label(
                self._left_frame, text="create password:"
            ),
            "Create": Button(self._left_frame, text="create", command=self.get_random_id),
            "Info text": Label(
                self._right_frame,
                text="This is a simple password generator. \nEnter a number for the amount of letters.\nOtherwise 15 letters will be the default.",
            ),
            "Output": Text(self._right_frame, width=40, height=5, pady=5, padx=15),
            "length": Label(self._left_frame, text="enter password length:"),
            "length_input": Entry(self._left_frame, textvariable=self._length),
        }
        return gui_elements

    def create_gui_elements(self):
        for key in self._gui_elements:
            self._gui_elements[key].pack(pady=5, padx=5)
        self._gui_elements["Output"].insert(END, "Output: ")
        
    def check_length(self, length):
        try:
            l = int(length)
        except ValueError:
            return False
        return l

    def get_random_id(self):
        l = self._length.get()
        length = self.check_length(l)
        if not length:
            length = "15"
        self._clear_gui()
        id = create_random_id(int(length))
        self._gui_elements["Output"].insert(END, id)


    def _clear_gui(self):
        self._gui_elements["Output"].delete(0.0, END)


def main():
    gui = RandomGui()
    
main()