import tkinter as tk
from tela_inicial import abrir_tela_inicial

def main():
    root = tk.Tk()
    root.title("Dashboard - Automação Python")
    root.geometry("800x600")
    abrir_tela_inicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()