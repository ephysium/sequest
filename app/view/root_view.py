import tkinter as tk
from .control_view import ControlView
from .result_view import ResultView
from ..core.search import search

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
        self.__control_view.button.config(command=self.__populate_result)

        self.__result_view = ResultView(master=self)
        self.__result_view.grid(row=0, column=1, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        self.mainloop()

    def __populate_result(self):
        self.__result_view.tree.delete(*self.__result_view.tree.get_children())

        result = search(
            filepath=self.__control_view.file_view.tooltip.text,
            sequence_list=list(self.__control_view.query_view.sequence_view.listbox.get(0, tk.END)),
            case_sensitivity=False
        )

        for seq_num, seq_elem in enumerate(result, start=1):
            seq_num_write = False

            for line_number, line_statement in seq_elem:
                self.__result_view.tree.insert("", "end", values=(seq_num if seq_num_write is False else "", line_number, line_statement))
                seq_num_write = True


