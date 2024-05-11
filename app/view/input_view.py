import tkinter as tk

"""
    RootView.ControlView.QueryView.InputView
    +----------------------+----------------------+----------------------+
    | QueryLabel           | QueryEntry           | QueryButton          |
    | row=0, col=0         | row=0, col=1         | row=0, col=2         |
    +----------------------+----------------------+----------------------+
"""
class InputView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__label = tk.Label(master=self, text="Enter your query here:")
        self.__label.grid(row=0, column=0, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.__placeholder = "Enter your query here..."

        self.__input = tk.StringVar(master=self, value=self.__placeholder)
        self.__input.trace_add(mode="write", callback=self.__trigger_query_input_change)

        self.entry = tk.Entry(master=self, fg="grey", textvariable=self.__input) 
        self.entry.grid(row=0, column=1, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        self.entry.bind(sequence="<FocusIn>", func=self.__trigger_query_entry)
        self.entry.bind(sequence="<FocusOut>", func=self.__trigger_query_entry)
        self.entry.bind("<Return>", self.__trigger_query_entry)
        
        self.button = tk.Button(master=self, text="Add element", state="disabled")
        self.button.grid(row=0, column=2, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=2, weight=1)

    def __trigger_query_input_change(self, *args):
        if self.__input.get() != "":
            self.button.config(state="active")
            
        else:
            self.button.config(state="disabled")

    def __trigger_query_entry(self, event):
        if event.type == tk.EventType.FocusIn:
            if self.entry.get() == self.__placeholder and self.entry.cget("fg") == "grey":
                self.entry.delete(0, "end")
                self.entry.insert(0, "")
                self.entry.config(fg="black")

        elif event.type == tk.EventType.FocusOut:
            if self.entry.get() == "":
                self.entry.insert(0, self.__placeholder)
                self.entry.config(fg="grey")
                self.button.config(state="disabled")