from tkinter import Frame, ttk

class ResultView(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        tree = ttk.Treeview(self, columns=("Column 1", "Column 2", "Column 3"), show="headings")
        tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        tree.configure(yscrollcommand=scrollbar.set)

        tree.heading("Column 1", text="Column 1")
        tree.heading("Column 2", text="Column 2")
        tree.heading("Column 3", text="Column 3")

        for i in range(50):
            tree.insert("", "end", values=(f"Item {i}", f"Value {i}", f"Description {i}"))