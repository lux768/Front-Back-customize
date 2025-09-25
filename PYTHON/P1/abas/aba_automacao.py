import tkinter as tk
import os
import subprocess
import tkinter as tk
from tkinter import scrolledtext

def criar_aba_automacao(notebook, abrir_tela_inicial, abrir_tela_logs, caminho_atual):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Automação")

    tk.Label(frame, text=f"Conteúdo de: {caminho_atual}", font=("Arial", 12)).pack()
    frame_scripts = tk.Frame(frame)
    frame_scripts.pack(pady=5)

    def executar_automacao(script_path):
        try:
            subprocess.Popen(["python", script_path])
            tk.messagebox.showinfo("Automação", f"Automação '{os.path.basename(script_path)}' iniciada!")
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao iniciar automação:\n{e}")

    tk.Label(frame, text="Controle Manual", font=("Arial", 12)).pack(pady=5)
    frame_botoes_exec = tk.Frame(frame)
    frame_botoes_exec.pack(pady=5)
    tk.Button(frame_botoes_exec, text="Iniciar", width=12, command=lambda: tk.messagebox.showinfo("Execução", "Execução manual iniciada.")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes_exec, text="Pausar", width=12, command=lambda: tk.messagebox.showinfo("Execução", "Execução manual pausada.")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes_exec, text="Parar", width=12, command=lambda: tk.messagebox.showinfo("Execução", "Execução manual parada.")).pack(side=tk.LEFT, padx=5)
    scrolledtext.ScrolledText(frame, width=45, height=7, state='disabled').pack(padx=10, pady=5)

    if not os.path.exists(caminho_atual):
        os.makedirs(caminho_atual)
        tk.Label(frame_scripts, text=f"Pasta '{caminho_atual}' criada. Adicione scripts Python nela.", fg="red").pack()
    else:
        itens = os.listdir(caminho_atual)
        pastas = [f for f in itens if os.path.isdir(os.path.join(caminho_atual, f))]
        scripts = [f for f in itens if f.endswith(".py") and os.path.isfile(os.path.join(caminho_atual, f))]

        if caminho_atual != "automacoes":
            pasta_anterior = os.path.dirname(caminho_atual)
            tk.Button(frame_scripts, text=".. (Voltar)", width=30,
                      command=lambda: abrir_tela_inicial(frame.master.master, abrir_tela_logs, pasta_anterior)).pack(pady=2)

        for pasta in pastas:
            tk.Button(frame_scripts, text=f"[Pasta] {pasta}", width=30,
                      command=lambda p=pasta: abrir_tela_inicial(frame.master.master, abrir_tela_logs, os.path.join(caminho_atual, p))).pack(pady=2)

        for script in scripts:
            script_path = os.path.join(caminho_atual, script)
            tk.Button(frame_scripts, text=script, width=30,
                      command=lambda s=script_path: executar_automacao(s)).pack(pady=2)

        if not pastas and not scripts:
            tk.Label(frame_scripts, text="Nenhuma automação ou pasta encontrada.", fg="red").pack()