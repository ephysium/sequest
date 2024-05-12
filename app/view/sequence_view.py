import tkinter as tk

"""
    App.ControlView.QueryView.SequenceView
    +---------------------------------+---------------------------------+
    | ElementListbox                  | ElementScrollbar                |
    | row=0, col=0                    | row=0, col=1                    |
    +---------------------------------+---------------------------------+
"""
class SequenceView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.element_listbox = tk.Listbox(master=self)
        self.element_listbox.grid(row=0, column=0, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.element_listbox.bind(sequence="<Button-1>", func=self.__on_item_hold)
        self.element_listbox.bind(sequence="<B1-Motion>", func=self.__on_item_drag)
        
        self.__element_scrollbar = tk.Scrollbar(master=self, orient="vertical", command=self.element_listbox.yview)
        self.__element_scrollbar.grid(row=0, column=1, sticky="ns")

        self.element_listbox.config(yscrollcommand=self.__element_scrollbar.set)

        self.__drag_data = {"index": None, "y": 0}

    def __on_item_hold(self, event):
        self.__drag_data["index"] = self.element_listbox.nearest(y=event.y)
        self.__drag_data["y"] = event.y

    def __on_item_drag(self, event):
        if self.__drag_data["index"] is not None:
            new_index = self.element_listbox.nearest(y=event.y)
            if new_index != self.__drag_data["index"]:
                items = list(self.element_listbox.get(first=0, last=tk.END))
                item = items.pop(self.__drag_data["index"])
                items.insert(new_index, item)
                self.element_listbox.delete(first=0, last=tk.END)
                for item in items:
                    self.element_listbox.insert(tk.END, item)
                self.__drag_data["index"] = new_index