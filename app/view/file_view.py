import os
import tkinter as tk
from tkinter import filedialog
from .util import Tooltip

"""
    App.ControlView.FileView
    +---------------------------------+---------------------------------+
    | FilenameEntry                   | BrowseButton                    |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class FileView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__filename = tk.StringVar(master=self, value="Get log file to extract...")
        
        self.__filename_entry = tk.Entry(master=self, fg="grey", state="disabled", cursor="", textvariable=self.__filename) 
        self.__filename_entry.grid(row=0, column=0, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        
        self.__browse_button = tk.Button(master=self, text="Browse", command=self.__trigger_browse_button)
        self.__browse_button.grid(row=0, column=1, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
    
        self.filepath_tooltip = Tooltip(master=self.__filename_entry, text="Filepath will display here in this tooltip", delay=500, wraplength=300, background="#ffffcc", foreground="#333333")

    def __trigger_browse_button(self):
        filepath = filedialog.askopenfilename(filetypes=[("LOG files", "*.log")])
        if filepath:
            self.__filename_entry.config(state="normal")
            self.__filename_entry.delete(first=0, last="end")
            max_chars = 30
            filename = os.path.basename(p=filepath)[-max_chars:]
            self.__filename.set(value=filename)
            self.__filename_entry.config(state="disabled")
            self.filepath_tooltip.text=filepath

            self.focus_force()