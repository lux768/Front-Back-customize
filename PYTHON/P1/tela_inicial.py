import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import subprocess
def escolher_e_executar_automacao(root):
    pasta = "automacoes"
    if not os.path.exists(pasta):
        messagebox.showerror("Erro", f"Pasta '{pasta}' não encontrada.")
        return

    scripts = [f for f in os.listdir(pasta) if f.endswith(".py")]
    if not scripts:
        messagebox.showinfo("Info", "Nenhuma automação encontrada na pasta.")
        return

    # Diálogo simples para escolher o script
    escolha = simpledialog.askstring("Escolher Automação",
                                     "Digite o nome do script para rodar:\n" +
                                     "\n".join(scripts))
    if escolha and escolha in scripts:
        caminho = os.path.join(pasta, escolha)
        try:
            subprocess.Popen(["python", caminho])
            messagebox.showinfo("Automação", f"Automação '{escolha}' iniciada!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao iniciar automação:\n{e}")
    elif escolha:
        messagebox.showwarning("Aviso", "Script não encontrado.")

def abrir_tela_inicial(root, abrir_tela_logs):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Bem-vindo à Automação Python!", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Iniciar Automação", width=20, command=lambda: escolher_e_executar_automacao(root)).pack(pady=10)
    tk.Button(root, text="Ver Logs", width=20, command=lambda: abrir_tela_logs(root, abrir_tela_inicial)).pack(pady=10)
    tk.Button(root, text="Sair", width=20, command=root.destroy).pack(pady=10)
