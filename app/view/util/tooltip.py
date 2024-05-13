import tkinter as tk

class Tooltip(object):
    def __init__(self, master, text="widget info", delay=500, wraplength=250, background="#ffffff", foreground="#000000"):
        self.delay = delay
        self.wraplength = wraplength
        self.master = master
        self.text = text
        self.background = background
        self.foreground = foreground

        self.master.bind(sequence="<Enter>", func=self.enter)
        self.master.bind(sequence="<Leave>", func=self.leave)
        self.id = None
        self.tooltip_window = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.master.after(ms=self.delay, func=self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.master.after_cancel(id=id_)

    def showtip(self, event=None):
        x, y, _, _ = self.master.bbox(column="insert")
        x += self.master.winfo_rootx() + 25
        y += self.master.winfo_rooty() + 20

        self.tooltip_window = tk.Toplevel(master=self.master)
        self.tooltip_window.wm_overrideredirect(boolean=True)
        self.tooltip_window.wm_geometry(newGeometry="+{}+{}".format(x, y))

        label = tk.Label(
            self.tooltip_window,
            text = self.text,
            justify = "left",
            background = self.background,
            foreground = self.foreground,
            relief = "solid",
            borderwidth = 1,
            wraplength = self.wraplength
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tooltip_window = self.tooltip_window
        self.tooltip_window = None
        if tooltip_window:
            tooltip_window.destroy()