import tkinter as tk
from tkinter import ttk
from abas.aba_automacao import criar_aba_automacao
from abas.aba_dados import criar_aba_dados
from abas.aba_logs import criar_aba_logs

def abrir_tela_inicial(root, caminho_atual="automacoes"):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Dashboard de Automação Python", font=("Arial", 16, "bold")).pack(pady=5)

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both', padx=5, pady=5)

    criar_aba_automacao(notebook, abrir_tela_inicial, caminho_atual)
    criar_aba_dados(notebook)
    criar_aba_logs(notebook)

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10)
    tk.Button(frame_botoes, text="Sair", width=15, command=root.destroy).pack(side=tk.LEFT, padx=5)
