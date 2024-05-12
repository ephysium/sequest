from tkinter import Frame, ttk

class ResultView(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.tree = ttk.Treeview(self, columns=("Log Sequence Number", "Log Line", "Log Statement"), show="headings")
        self.tree.grid(row=0, column=0, sticky="nswe")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.heading("Log Sequence Number", text="Log Sequence Number")
        self.tree.heading("Log Line", text="Log Line")
        self.tree.heading("Log Statement", text="Statement")