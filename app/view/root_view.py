import tkinter as tk
from .control_view import ControlView
from .result_view import ResultView
from ..core import StringSearchSequence

"""
    RootView
    +---------------------------------+---------------------------------+
    | ControlView                     | ResultView                      |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class RootView(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Sequest")
        self.geometry("1400x600")
        # self.resizable(False, False)
        
        self.__control_view = ControlView(master=self)
        self.__control_view.grid(row=0, column=0, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.__control_view.search_button.config(command=self.__populate_result)

        self.__result_view = ResultView(master=self)
        self.__result_view.grid(row=0, column=1, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        self.mainloop()

    def __populate_result(self):
        self.__result_view.result_treeview.delete(*self.__result_view.result_treeview.get_children())

        result = StringSearchSequence(
            target_filepath=self.__control_view.file_view.filepath_tooltip.text,
            input_list=list(self.__control_view.query_view.sequence_view.element_listbox.get(0, tk.END)),
            case_sensitivity=self.__control_view.query_view.boolean_view.case_sensitivity.get(),
            sequential_log_lines=self.__control_view.query_view.boolean_view.successive_log_lines.get()
        ).execute()

        if result:
            for sequence_no, sequence_instance in enumerate(result, start=1):
                show_sequence_no = False

                for log in sequence_instance:
                    self.__result_view.result_treeview.insert("", "end", values=(sequence_no if show_sequence_no is False else "", log["log_line"], log["log_statement"]))
                    show_sequence_no = True


