import tkinter as tk
from .file_view import FileView
from .type_view import TypeView
from .query_view import QueryView

"""
    RootView.ControlView
    +----------------------+
    | FileView             |
    | row=0, col=0         |
    +----------------------+
    | TypeView             |
    | row=1, col=0         |
    +----------------------+
    | QueryView            |
    | row=2, col=0         |
    +----------------------+
    | Button               |
    | row=3, col=0         |
    +----------------------+
"""
class ControlView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.__file_view = FileView(master=self)
        self.__file_view.grid(row=0, column=0, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.__type_view = TypeView(master=self)
        self.__type_view.grid(row=1, column=0, sticky="we")
        self.grid_rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.__log_input_view = QueryView(master=self)
        self.__log_input_view.grid(row=2, column=0, sticky="we")
        self.grid_rowconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.button = tk.Button(master=self, text="Search")
        self.button.grid(row=3, column=0, sticky="we")
        self.grid_rowconfigure(index=3, weight=1)
        self.grid_columnconfigure(index=0, weight=1)