import tkinter as tk
from tkinter import scrolledtext

def criar_aba_historico(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Histórico/Logs")

    tk.Label(frame, text="Execuções Anteriores", font=("Arial", 12)).pack(pady=5)
    historico_area = scrolledtext.ScrolledText(frame, width=45, height=10, state='normal')
    historico_area.pack(padx=10, pady=5)
    historico_area.insert(tk.END, "2025-09-22 10:00:01 - SUCESSO - Automação X\n2025-09-22 10:05:01 - ERRO - Automação Y\n")
    historico_area.config(state='disabled')
