from pydoc import text
import tkinter as tk
import tkinter.ttk as ttk
import sys
import time


class digitalClock:
    def __init__(self, root, title) -> None:
        self._root = root
        self._root.title(title)

        self._clock = ttk.Label()
        self._ot = ttk.Label(text='Ofek Sasson')
        self._clock.pack()
        self._ot.pack()

        self.getTime()

        self._root.mainloop()

    def getTime(self):
        var = time.strftime("%I:%M:%S %p")
        self._clock.config(text=var)
        self._clock.after(200, self.getTime)


root = tk.Tk()
clock = digitalClock(root, "Digital Clock")
