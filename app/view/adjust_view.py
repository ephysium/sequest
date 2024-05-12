import tkinter as tk

"""
    App.ControlView.QueryView.AdjustView
    +---------------------------------+---------------------------------+
    | EditButtom                      | RemoveButton                    |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class AdjustView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.edit_button = tk.Button(master=self, text="Edit", state="disabled")
        self.edit_button.grid(row=0, column=0, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.remove_button = tk.Button(master=self, text="Remove", state="disabled")
        self.remove_button.grid(row=0, column=1, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)