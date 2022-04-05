from tkinter import *
from tkinter import filedialog

class App(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(720, 480)


app = App()
app.mainloop()