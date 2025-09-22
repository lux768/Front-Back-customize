import tkinter as tk
from tela_inicial import abrir_tela_inicial

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dashboard - Automação Python")
    root.geometry("400x300")
    abrir_tela_inicial(root)
    root.mainloop()
