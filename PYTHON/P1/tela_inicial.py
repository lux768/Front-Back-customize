import tkinter as tk
from tkinter import ttk
from abas.aba_automacao import criar_aba_automacao
from abas.aba_execucao import criar_aba_execucao
from abas.aba_upload import criar_aba_upload
from abas.aba_historico import criar_aba_historico
from abas.aba_relatorios import criar_aba_relatorios
from abas.aba_notificacoes import criar_aba_notificacoes
from abas.aba_ajuda import criar_aba_ajuda

def abrir_tela_inicial(root, abrir_tela_logs, caminho_atual="automacoes"):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Dashboard de Automação Python", font=("Arial", 16, "bold")).pack(pady=5)

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both', padx=5, pady=5)

    # Cada aba é criada por um arquivo separado
    criar_aba_automacao(notebook, abrir_tela_inicial, abrir_tela_logs, caminho_atual)
    criar_aba_execucao(notebook)
    criar_aba_upload(notebook)
    criar_aba_historico(notebook)
    criar_aba_relatorios(notebook)
    criar_aba_notificacoes(notebook)
    criar_aba_ajuda(notebook)

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10)
    tk.Button(frame_botoes, text="Ver Logs", width=15, command=lambda: abrir_tela_logs(root, abrir_tela_inicial)).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes, text="Sair", width=15, command=root.destroy).pack(side=tk.LEFT, padx=5)
