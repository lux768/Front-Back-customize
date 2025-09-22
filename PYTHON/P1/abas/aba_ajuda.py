import tkinter as tk

def criar_aba_ajuda(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Ajuda/Suporte")

    tk.Label(frame, text="FAQ e Suporte", font=("Arial", 12)).pack(pady=5)
    tk.Label(frame, text="• Como usar o sistema?\n• Contato do suporte: suporte@empresa.com\n• Tutoriais rápidos: ...").pack(pady=5)
