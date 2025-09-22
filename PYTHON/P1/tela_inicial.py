import tkinter as tk
from tela_logs import abrir_tela_logs

def abrir_tela_inicial(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Bem-vindo à Automação Python!", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Ver Logs", width=20, command=lambda: abrir_tela_logs(root)).pack(pady=20)
    tk.Button(root, text="Sair", width=20, command=root.destroy).pack(pady=10)
