import tkinter as tk
from .input_view import InputView
from .boolean_view import BooleanView
from .sequence_view import SequenceView
from .adjust_view import AdjustView
from .util import Dialog

"""
    App.ControlView.QueryView
    +---------------------------------+
    | InputView                       |
    | row=0, col=0                    |
    +---------------------------------+
    | BooleanView                     |
    | row=1, col=0                    |
    +---------------------------------+
    | SequenceView                    |
    | row=2, col=0                    |
    +---------------------------------+
    | AdjustView                      |
    | row=3, col=0                    |
    +---------------------------------+
"""
class QueryView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__target_item_index = None

        self.input_view = InputView(master=self)
        self.input_view.grid(row=0, column=0, sticky="we")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.input_view.element_entry.bind(sequence="<Return>", func=self.__add_input)
        self.input_view.add_button.config(command=self.__add_input)
        
        self.boolean_view = BooleanView(master=self)
        self.boolean_view.grid(row=1, column=0, sticky="nswe")
        self.grid_rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        
        self.sequence_view = SequenceView(master=self)
        self.sequence_view.grid(row=2, column=0, sticky="we")
        self.grid_rowconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.sequence_view.element_listbox.bind(sequence="<ButtonRelease-1>", func=self.__select_item)

        self.__adjust_view = AdjustView(master=self)
        self.__adjust_view.grid(row=3, column=0, sticky="we")
        self.grid_rowconfigure(index=3, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.__adjust_view.edit_button.config(command=self.__edit_selected)
        self.__adjust_view.remove_button.config(command=self.__remove_selected)

    def __add_input(self, *args):
        input = self.input_view.element_entry.get()
        if input:
            self.sequence_view.element_listbox.insert(tk.END, input)
            self.input_view.element_entry.delete(first=0, last=tk.END)

    def __select_item(self, *args):
        selected_index = self.sequence_view.element_listbox.curselection()
        if selected_index:
            self.__target_item_index = int(selected_index[0])
            self.__adjust_view.edit_button.config(state="normal")
            self.__adjust_view.remove_button.config(state="normal")

    def __edit_selected(self):
        if self.__target_item_index is not None:
            target_value = self.sequence_view.element_listbox.get(first=self.__target_item_index)
            dialog = Dialog(self.master.master, title="Confirm Edit", text="Edit element:", show_entry=True, initial_value=target_value)
            if dialog.result is not None:
                self.sequence_view.element_listbox.delete(first=self.__target_item_index)
                self.sequence_view.element_listbox.insert(self.__target_item_index, dialog.result)
                self.__adjust_view.edit_button.config(state="disabled")
                self.__adjust_view.remove_button.config(state="disabled")

    def __remove_selected(self):
        if self.__target_item_index is not None:
            target_value = self.sequence_view.element_listbox.get(self.__target_item_index)
            dialog = Dialog(self.master.master, title="Confirm Deletion", text="Are you sure you want to delete '{}'?".format(target_value))
            if dialog.result is not None:
                self.sequence_view.element_listbox.delete(self.__target_item_index)
                self.__adjust_view.edit_button.config(state="disabled")
                self.__adjust_view.remove_button.config(state="disabled")