# Notepad using the Tkinter library 

# Importing the libraries -------------------------------

import tkinter as tk 
from tkinter import filedialog 

# Creating the classes ----------------------------------

class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Putting the title for Notepad -----------------

        self.title("Bloco de notas Z")

        # Creating a text widget ------------------------

        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        # Creating a menu bar ---------------------------

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Creating a file menu --------------------------

        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.quit)

        # Creating a edit menu --------------------------

        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Cortar", command=self.cut)
        edit_menu.add_command(label="Copiar", command=self.copy)
        edit_menu.add_command(label="Pasta", command=self.paste)

    # New file ------------------------------------------
    
    def new_file(self):
        self.text.delete("1.0", "end")
        self.title("Bloco de Notas Z")
    
    # Open file -----------------------------------------

    def open_file(self):
        file = filedialog.askopenfile(parent=self, mode="rb", title="Abrir um arquivo")
        if file:
            contents = file.read()
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)
            file.close()
            self.title(file.name + " - Bloco de Notas Z")

    # Save file -----------------------------------------

    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file: 
            contents = self.text.get("1.0", "end")
            file.write(contents)
            file.close()
            self.title(file.name + " - Bloco de Notas Z")

    
    # Cut -----------------------------------------------

    def cut(self):
        self.text.event_generate("<<Cortar>>")

    # Copy ----------------------------------------------

    def copy(self):
        self.text.event_generate("<<Copiar>>")

    def paste(self):
        self.text.event_generate("<<Pasta>>")
    
# Starting ----------------------------------------------

if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop()
