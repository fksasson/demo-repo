import tkinter as tk
import tkinter.ttk as ttk


class window:
    def __init__(self, root, title) -> None:
        self._root = root
        self._root.title(title)
        self._root.resizable(width=False, height=False)

        # input temp:
        self._frm_inputs = ttk.Frame(master=self._root)
        self._ent_fahrenheit = ttk.Entry(master=self._frm_inputs, width=10)
        self._lbl_fahrenheit = ttk.Label(
            master=self._frm_inputs,
            text='\N{DEGREE FAHRENHEIT}'
        )
        self._ent_celsius = ttk.Entry(master=self._frm_inputs, width=10)
        self._lbl_celsius = ttk.Label(
            master=self._frm_inputs,
            text='\N{DEGREE CELSIUS}'
        )

        self._ent_fahrenheit.grid(row=0, column=0, sticky='e')
        self._lbl_fahrenheit.grid(row=0, column=1, sticky='w')
        self._ent_celsius.grid(row=1, column=0, sticky='e')
        self._lbl_celsius.grid(row=1, column=1, sticky='w')
        self._frm_inputs.grid(row=0, column=0, padx=10)

        # convert button
        self._btn_convertFtC = ttk.Button(
            master=self._frm_inputs,
            text='\N{RIGHTWARDS BLACK ARROW}',
            width=3,
            command=self.fahrenheitToCelsius
        )
        self._lbl_resultFtC = ttk.Label(
            master=self._frm_inputs,
            text='\N{DEGREE CELSIUS}'
        )
        self._btn_convertCtF = ttk.Button(
            master=self._frm_inputs,
            text='\N{RIGHTWARDS BLACK ARROW}',
            width=3,
            command=self.celsiusToFahrenheit
        )
        self._lbl_resultCtF = ttk.Label(
            master=self._frm_inputs,
            text='\N{DEGREE FAHRENHEIT}'
        )
        self._ot = ttk.Label(text='Ofek Sasson')
        self._btn_convertFtC.grid(row=0, column=2, pady=10)
        self._lbl_resultFtC.grid(row=0, column=3, padx=10)
        self._btn_convertCtF.grid(row=1, column=2, pady=10)
        self._lbl_resultCtF.grid(row=1, column=3, padx=10)
        self._ot.grid()
        
        self._root.mainloop()

    def fahrenheitToCelsius(self):
        fahrenheit = float(self._ent_fahrenheit.get())
        celsius = (5/9)*(fahrenheit-32)
        self._lbl_resultFtC['text'] = f'{round(celsius,2)} \N{DEGREE CELSIUS}'

    def celsiusToFahrenheit(self):
        celsius = float(self._ent_celsius.get())
        fahrenheit = ((9/5)*celsius) + 32
        self._lbl_resultCtF['text'] = f'{round(fahrenheit,2)}\N{DEGREE FAHRENHEIT}'


root = tk.Tk()
window_1 = window(root, 'Temperature Converter')


