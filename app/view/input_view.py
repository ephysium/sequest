import tkinter as tk

"""
    RootView.ControlView.QueryView.InputView
    +---------------------------------+---------------------------------+
    | QueryEntry                      | QueryButton                     |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class InputView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__element_placeholder = "Add log here"

        self.__element_input = tk.StringVar(master=self, value=self.__element_placeholder)
        self.__element_input.trace_add(mode="write", callback=self.__trigger_query_input_change)

        self.element_entry = tk.Entry(master=self, fg="grey", textvariable=self.__element_input) 
        self.element_entry.grid(row=0, column=0, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.element_entry.bind(sequence="<FocusIn>", func=self.__trigger_query_entry)
        self.element_entry.bind(sequence="<FocusOut>", func=self.__trigger_query_entry)
        self.element_entry.bind("<Return>", self.__trigger_query_entry)
        
        self.add_button = tk.Button(master=self, text="Add log", state="disabled")
        self.add_button.grid(row=0, column=1, sticky="nswe")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)

    def __trigger_query_input_change(self, *args):
        if self.__element_input.get() != "":
            self.add_button.config(state="active")
            
        else:
            self.add_button.config(state="disabled")

    def __trigger_query_entry(self, event):
        if event.type == tk.EventType.FocusIn:
            if self.element_entry.get() == self.__element_placeholder and self.element_entry.cget("fg") == "grey":
                self.element_entry.delete(0, "end")
                self.element_entry.insert(0, "")
                self.element_entry.config(fg="black")

        elif event.type == tk.EventType.FocusOut:
            if self.element_entry.get() == "":
                self.element_entry.insert(0, self.__element_placeholder)
                self.element_entry.config(fg="grey")
                self.add_button.config(state="disabled")