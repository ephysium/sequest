import tkinter as tk

"""
    RootView.ControlView.QueryView.InputView.BooleanView
    +---------------------------------+---------------------------------+
    | CaseSensitivityCheckbutton      | SuccessiveLogLinesCheckbutton   |
    | row=1, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class BooleanView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.case_sensitivity = tk.BooleanVar()

        self.__case_sensitivity_checkbutton = tk.Checkbutton(master=self, text="Enable Case Sensitive", variable=self.case_sensitivity)
        self.__case_sensitivity_checkbutton.grid(row=1, column=0, sticky="w")
        # self.grid_rowconfigure(index=1, weight=1)
        # self.grid_columnconfigure(index=0, weight=1)

        self.successive_log_lines = tk.BooleanVar()

        self.__successive_log_lines_checkbutton = tk.Checkbutton(master=self, text="Enable Successive Log Lines", variable=self.successive_log_lines)
        self.__successive_log_lines_checkbutton.grid(row=1, column=1, sticky="w")
        # self.grid_rowconfigure(index=1, weight=1)
        # self.grid_columnconfigure(index=1, weight=1)