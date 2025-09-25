import tkinter as tk
from tela_inicial import abrir_tela_inicial

def main():
    root = tk.Tk()
    root.title("Dashboard - Automação Python")
    root.geometry("800x600")
    # Passe uma função dummy para abrir_tela_logs, já que agora está tudo nas abas
    abrir_tela_inicial(root, lambda *args, **kwargs: None)
    root.mainloop()

if __name__ == "__main__":
    main()
