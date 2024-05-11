import tkinter as tk
from .control_view import ControlView
from .result_view import ResultView

"""
    RootView
    +----------------------+----------------------+
    | ControlView          | ResultView           |
    | row=0, col=0         | row=0, col=1         |
    +----------------------+----------------------+
"""
class RootView(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Sequest")
        self.geometry("1400x600")
        self.resizable(False, False)
        
        self.__control_view = ControlView(master=self)
        self.__control_view.grid(row=0, column=0, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.__control_view.button.config(command=self.search)

        self.__result_view = ResultView(master=self)
        self.__result_view.grid(row=0, column=1, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        self.mainloop()

    def search(self):
        pass
