import tkinter as tk
import tkinter.simpledialog as simpledialog

class Dialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, text=None, show_entry=False, initial_value="", width=400, height=120, resizeable_x=False, resizeable_y=False):
        self.text = text
        self.show_entry = show_entry
        self.initial_value = initial_value
        self.width = width
        self.height = height
        self.resizeable_x = resizeable_x
        self.resizeable_y = resizeable_y

        super().__init__(parent, title=title)
        
    def body(self, *args):
        self.geometry("{}x{}".format(self.width, self.height))
        self.resizable(self.resizeable_x, self.resizeable_y)
        self.config(padx=10, pady=10)
        
        box = tk.Frame(self)

        if self.show_entry:
            self.entry_label = tk.Label(box, text=self.text)
            self.entry_label.grid(row=0, column=0, sticky="nswe")
            box.grid_rowconfigure(index=0, weight=1)
            box.grid_columnconfigure(index=0, weight=1)

            self.entry = tk.Entry(box)
            self.entry.grid(row=1, column=0, sticky="nswe")
            self.entry.insert(0, self.initial_value)
            box.grid_rowconfigure(index=1, weight=1)
            box.grid_columnconfigure(index=0, weight=1)
        else:
            self.label = tk.Label(box, text=self.text)
            self.label.grid(row=0, column=0, sticky="nswe")
            box.grid_rowconfigure(index=0, weight=1)
            box.grid_columnconfigure(index=0, weight=1)

        box.pack(fill="both", expand=True)

    def buttonbox(self):
        box = tk.Frame(self)

        ok_button = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        ok_button.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        box.grid_rowconfigure(index=0, weight=1)
        box.grid_columnconfigure(index=0, weight=1)

        cancel_button = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        cancel_button.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        box.grid_rowconfigure(index=0, weight=1)
        box.grid_columnconfigure(index=1, weight=1)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack(side="bottom", fill="x")

    def apply(self):
        if self.show_entry:
            self.result = self.entry.get()
        else:
            self.result = "ok"
