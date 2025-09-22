import tkinter as tk
from tkinter import scrolledtext

def criar_aba_execucao(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Execução Manual")

    tk.Label(frame, text="Controle Manual", font=("Arial", 12)).pack(pady=5)
    frame_botoes_exec = tk.Frame(frame)
    frame_botoes_exec.pack(pady=5)
    tk.Button(frame_botoes_exec, text="Iniciar", width=12, command=lambda: tk.messagebox.showinfo("Execução", "Execução manual iniciada.")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes_exec, text="Pausar", width=12, command=lambda: tk.messagebox.showinfo("Execução", "Execução manual pausada.")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes_exec, text="Parar", width=12, command=lambda: tk.messagebox.showinfo("Execução", "Execução manual parada.")).pack(side=tk.LEFT, padx=5)
    scrolledtext.ScrolledText(frame, width=45, height=7, state='disabled').pack(padx=10, pady=5)
