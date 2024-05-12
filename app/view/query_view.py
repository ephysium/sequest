import tkinter as tk
from tkinter import simpledialog, messagebox
from .input_view import InputView
from .sequence_view import SequenceView
from .adjust_view import AdjustView
from .util import Dialog

"""
    App.ControlView.QueryView
    +----------------------+
    | InputView            |
    | row=0, col=0         |
    +----------------------+
    | SequenceView         |
    | row=1, col=0         |
    +----------------------+
    | AdjustView           |
    | row=2, col=0         |
    +----------------------+
"""
class QueryView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__target_item_index = None

        self.__input_view = InputView(master=self)
        self.__input_view.grid(row=1, column=0, sticky="we")
        self.grid_rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.__input_view.entry.bind(sequence="<Return>", func=self.__add_input)
        self.__input_view.button.config(command=self.__add_input)
        
        self.sequence_view = SequenceView(master=self)
        self.sequence_view.grid(row=2, column=0, sticky="we")
        self.grid_rowconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.sequence_view.listbox.bind(sequence="<ButtonRelease-1>", func=self.select_item)

        self.__adjust_view = AdjustView(master=self)
        self.__adjust_view.grid(row=3, column=0, sticky="we")
        self.grid_rowconfigure(index=3, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.__adjust_view.edit_button.config(command=self.edit_selected)
        self.__adjust_view.remove_button.config(command=self.remove_selected)

    def __add_input(self, *args):
        input = self.__input_view.entry.get()
        if input:
            self.sequence_view.listbox.insert(tk.END, input)
            self.__input_view.entry.delete(first=0, last=tk.END)

    def select_item(self, *args):
        selected_index = self.sequence_view.listbox.curselection()
        if selected_index:
            self.__target_item_index = int(selected_index[0])
            self.__adjust_view.edit_button.config(state="normal")
            self.__adjust_view.remove_button.config(state="normal")

    def edit_selected(self):
        if self.__target_item_index is not None:
            target_value = self.sequence_view.listbox.get(first=self.__target_item_index)
            dialog = Dialog(self.master.master, title="Confirm Edit", text="Edit element:", show_entry=True, initial_value=target_value)
            if dialog.result is not None:
                self.sequence_view.listbox.delete(first=self.__target_item_index)
                self.sequence_view.listbox.insert(self.__target_item_index, dialog.result)
                self.__adjust_view.edit_button.config(state="disabled")
                self.__adjust_view.remove_button.config(state="disabled")

    def remove_selected(self):
        if self.__target_item_index is not None:
            target_value = self.sequence_view.listbox.get(self.__target_item_index)
            dialog = Dialog(self.master.master, title="Confirm Deletion", text="Are you sure you want to delete '{}'?".format(target_value))
            if dialog.result is not None:
                self.sequence_view.listbox.delete(self.__target_item_index)
                self.__adjust_view.edit_button.config(state="disabled")
                self.__adjust_view.remove_button.config(state="disabled")