import tkinter as tk

"""
    RootView.ControlView.TypeView
    +---------------------------------+---------------------------------+
    | StringButton                    | RegexButton                     |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class TypeView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__string_button = tk.Button(master=self, text="String Search", relief=tk.SUNKEN, command=lambda: self.__toggle_active_button(self.__string_button))
        self.__string_button.grid(row=0, column=0, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.__regex_button = tk.Button(master=self, text="Regex Search", command=lambda: self.__toggle_active_button(self.__regex_button))
        self.__regex_button.grid(row=0, column=1, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)

        self.active_button = self.__string_button
        
    def __toggle_active_button(self, clicked_button):
        if self.active_button != clicked_button:
            if self.active_button:
                self.active_button.config(relief=tk.RAISED)
            clicked_button.config(relief=tk.SUNKEN)
            self.active_button = clicked_button
