from cgitb import text
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.ttk as ttk


class textEditor:
    def __init__(self, root=tk.Tk(), title="Text Editor") -> None:
        self.root = root
        self.title = title
        self.root.title(self.title)
        self.root.rowconfigure(0, minsize=400, weight=1)
        self.root.columnconfigure(1, minsize=800, weight=1)

        self.frm_buttons = ttk.Frame(master=self.root)
        self.btn_open = ttk.Button(
            master=self.frm_buttons,
            text='Open',
            command=self.open_file)
        self.btn_save = ttk.Button(
            master=self.frm_buttons,
            text='Save',
            command=self.save_file)
        self.txt_edit = tk.Text(master=self.root)
        self.frm_buttons.grid(row=0, column=0, sticky='ns')
        self.btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.btn_save.grid(row=1, column=0, sticky='ew', padx=5)
        self.txt_edit.grid(row=0, column=1, sticky="nesw")

        self.root.mainloop()

    def open_file(self):
        """opens a file for editing"""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.txt_edit.delete("1.0", tk.END)
        with open(filepath, 'r', encoding='utf-8') as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
        self.root.title(f"{self.title} - {filepath.split('/')[-1].split('.')[0]}")

    def save_file(self):
        """saves the current file as a new file"""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
        if not filepath:
            return
        with open(filepath, 'w', encoding="utf-8") as output_file:
            text = self.txt_edit.get('1.0', tk.END)
            output_file.write(text)            
        self.root.title(f"{self.title} - {filepath.split('/')[-1].split('.')[0]}")


window = textEditor()
