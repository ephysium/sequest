import os
import tkinter as tk
from tkinter import filedialog
from .util import Tooltip

"""
    App.ControlView.FileView
    +----------------------+----------------------+----------------------+
    | Label                | Entry                | Button               |
    | row=0, col=0         | row=0, col=1         | row=0, col=2         |
    +----------------------+----------------------+----------------------+
"""
class FileView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__label = tk.Label(master=self, text="Browse log file:")
        self.__label.grid(row=0, column=0, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.__input = tk.StringVar(master=self, value="Get log file to extract...")
        
        self.__entry = tk.Entry(master=self, fg="grey", state="disabled", cursor="", textvariable=self.__input) 
        self.__entry.grid(row=0, column=1, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        self.__button = tk.Button(master=self, text="Browse", command=self.__trigger_browse_button)
        self.__button.grid(row=0, column=2, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=2, weight=1)
    
        self.tooltip = Tooltip(master=self.__entry, text="Filepath will display here in this tooltip", delay=500, wraplength=300, background="#ffffcc", foreground="#333333")

    def __trigger_browse_button(self):
        filepath = filedialog.askopenfilename(filetypes=[("LOG files", "*.log")])
        if filepath:
            self.__entry.config(state="normal")
            self.__entry.delete(first=0, last="end")
            max_chars = 30
            filename = os.path.basename(p=filepath)[-max_chars:]
            self.__input.set(value=filename)
            self.__entry.config(state="disabled")
            self.tooltip.text=filepath