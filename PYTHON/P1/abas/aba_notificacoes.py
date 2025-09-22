import tkinter as tk
from tkinter import scrolledtext
def criar_aba_notificacoes(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Notificações")

    tk.Label(frame, text="Notificações", font=("Arial", 12)).pack(pady=5)
    notificacoes_area = scrolledtext.ScrolledText(frame, width=45, height=7, state='normal')
    notificacoes_area.pack(padx=10, pady=5)
    notificacoes_area.insert(tk.END, "Nenhuma notificação no momento.\n")
    notificacoes_area.config(state='disabled')
