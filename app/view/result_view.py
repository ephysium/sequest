from tkinter import Frame, ttk

"""
    App.ResultView
    +---------------------------------+---------------------------------+
    | ResultTreeview                  | ResultScrollbar                 |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class ResultView(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.result_treeview = ttk.Treeview(self, columns=("Log Sequence Number", "Log Line", "Log Statement"), show="headings")
        self.result_treeview.grid(row=0, column=0, sticky="nswe")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__result_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.result_treeview.yview)
        self.__result_scrollbar.grid(row=0, column=1, sticky="ns")

        self.result_treeview.configure(yscrollcommand=self.__result_scrollbar.set)

        self.result_treeview.heading("Log Sequence Number", text="Log Sequence Number")
        self.result_treeview.heading("Log Line", text="Log Line")
        self.result_treeview.heading("Log Statement", text="Statement")