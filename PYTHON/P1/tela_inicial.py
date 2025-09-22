import tkinter as tk

def abrir_tela_inicial(root, abrir_tela_logs):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Bem-vindo à Automação Python!", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Ver Logs", width=20, command=lambda: abrir_tela_logs(root, abrir_tela_inicial)).pack(pady=20)
    tk.Button(root, text="Sair", width=20, command=root.destroy).pack(pady=10)
