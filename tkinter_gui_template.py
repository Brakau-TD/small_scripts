from tkinter import * # type: ignore

class AppGui:
    """
    simple Tkinter GUI
    can be adapted via the _information dictionary 
    the _gui_elements dictionary
    """

    def __init__(self):
        '''
        initializes the Gui
        main attributes: 
        self._text_variables: list, self._listvariables: list[], self._radio: StringVar
        two methods are attached to the two buttons in the example
        the radio-buttons offer more options for the user
        two entry fields are also available
        variables and gui elements can be added in the initialize_variables and 
        initialize_dictionary methods. They are created dynamically.
        '''
        self._text_variables: list = []
        self._listvariables: list = []
        self._radio: StringVar

        self._information: dict = {
            "appname": "My App",
            "title": "My App",
            "description": "This is my app. It does something.",
            "width": 480,
            "height": 480,
            "padx": 10,
            "pady": 10,
        }
        self.create_window()
    
    def initialize_variables(self):
        '''initializes the variables'''
        variable_dictionary = {
            "text_variables": [self._text_variables, 4],
            "listvariables": [self._listvariables, 4],
        }
        for element in variable_dictionary:
            for _ in range(variable_dictionary[element][1]):
                variable_dictionary[element][0].append(StringVar())
        
        self._radio = StringVar()

    def initialize_dictionary(self) -> dict:
        '''contains the general layout of the gui as a dictionary'''
        gui_elements = {
            "Labels": {
                "L1": Label(
                    self._top_frame,
                text="Top-Frame description",
                justify = "left"
                ),
                "L2": Label(
                    self._left_frame,
                text="Left-Frame description",
                justify = "left"
                ),
                "L3": Label(
                    self._right_frame,
                text="Right-Frame description",
                justify = "right"
                ),
                "L4": Label(
                    self._bottom_frame,
                text="Bottom-Frame description",
                justify = "right"
                ),
            },
            "Buttons": {
                "B1": Button(
                    self._left_frame,
                text="Button 1",
                command=lambda : self.menu("button1"),
                justify="left"
                ),
                "B2": Button(
                    self._left_frame,
                text="Button 2",
                command=lambda : self.menu("button2"),
                justify="left"
                ),
            },
            "Entries": {
                "E1": Entry(
                    self._left_frame,
                textvariable=self._text_variables[0]
                ),
                "E2": Entry(
                    self._left_frame,
                textvariable=self._text_variables[1]
                ),
            },
            "Text": {
                "T1": Text(
                    self._left_frame,
                height = 5,
                width = 30,
                wrap = WORD
                ),
                "T2": Text(
                    self._right_frame,
                height = 5,
                width = 30,
                wrap = WORD
                ),
            },
            "Listboxes": {
                "L3": Listbox(
                    self._right_frame,
                              listvariable=self._listvariables[0],
                              height=5,
                              width=50,
                              selectmode=SINGLE),  
            },
            "Radiobuttons": {
                "R1": Radiobutton(
                    self._left_frame,
                text="Description",
                variable=self._radio,
                value="Radiobutton 1 is pressed",
                state="normal"
                ),
                "R2": Radiobutton(
                    self._left_frame,
                text="Description",
                variable=self._radio,
                value="radiobutton 2 is pressed",
                state="normal"
                ),
            },
        }
        return gui_elements

    def create_window(self):
        self._app = Tk()
        title = self._information["appname"] # type: ignore
        self._app.title(title) # type: ignore
        self._app.geometry(
            f'{self._information["width"]}x{self._information["height"]}') # type: ignore    
        self.create_frames()
        self.create_gui_elements()
        self._clear_gui()
        self._app.mainloop()

    def create_frames(self):
        self._left_frame = Frame(self._app, height = 10, width = 50)
        self._left_frame.grid(row = 1, column = 0, sticky = "w")
        self._right_frame = Frame(self._app, height = 10, width = 50)
        self._right_frame.grid(row = 1, column = 1, sticky = "e")
        self._top_frame = Frame(self._app, height = 10, width = 100)
        self._top_frame.grid(row = 0, column = 0, sticky = "n")
        self._bottom_frame = Frame(self._app, height = 10, width = 100)
        self._bottom_frame.grid(row = 2, column = 0, sticky = "s")

    def create_gui_elements(self):
        '''creates the gui elements from dictionaries'''
        self.initialize_variables()
        self._gui_elements = self.initialize_dictionary()
        keys = list(self._gui_elements.keys())
        self._create_gui(keys)
        
    def _create_gui(self, keys):
        '''packs the gui elements into the frames'''
        for key in keys:
            for element in self._gui_elements[key]:
                self._gui_elements[key][element].pack(
                    pady=self._information["pady"], # type: ignore
                    padx=self._information["padx"], # type: ignore
                    side="top",
                    anchor="w",
                    )

    def menu(self, choice: str):
        '''this function will be triggered by the buttons'''
        match choice:
            case "button1":
                self.app_function_one()
            case "button2":
                self.app_function_two()
        self._clear_gui()
    

    def _clear_gui(self):
        '''this function will be called to clear the gui'''
        to_clean = ["Text", "Listboxes","Entries","Radiobuttons"]
        for element in to_clean:
            match element:
                case "Text":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].delete(1.0, END)
                case "Listboxes":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].delete(0, END)
                case "Entries":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].delete(0, END)
                case "Radiobuttons":
                    for key in self._gui_elements[element]:
                        self._gui_elements[element][key].deselect()

        return

    def app_function_one(self):
        '''this function will be assigned to the first button'''
        return

    def app_function_two(self):
        '''this function will be assigned to the second button'''
        return    

def main():
    gui = AppGui()
    
main()