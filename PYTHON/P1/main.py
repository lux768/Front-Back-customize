import tkinter as tk
from tela_inicial import abrir_tela_inicial
from tela_logs import abrir_tela_logs

def main():
    root = tk.Tk()
    root.title("Dashboard - Automação Python")
    root.geometry("400x300")
    abrir_tela_inicial(root, abrir_tela_logs)
    root.mainloop()

if __name__ == "__main__":
    main()
