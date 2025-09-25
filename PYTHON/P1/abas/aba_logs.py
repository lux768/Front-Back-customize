import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def criar_aba_logs(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Logs")

    # Configuração do grid principal
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    # --- Lado Esquerdo: Logs da Automação ---
    frame_esquerda = tk.Frame(frame)
    frame_esquerda.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    frame_esquerda.columnconfigure(0, weight=1)

    tk.Label(frame_esquerda, text="Logs da Automação", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w", pady=5)

    log_area = scrolledtext.ScrolledText(frame_esquerda, width=60, height=15, state='normal')
    log_area.grid(row=1, column=0, sticky="nsew", pady=5)
    logs = [
        "2025-09-22 10:00:01 - INFO - Automação iniciada.",
        "2025-09-22 10:00:05 - SUCCESS - Processamento concluído.",
        "2025-09-22 10:01:10 - ERROR - Falha ao acessar arquivo.",
        "2025-09-22 10:02:00 - INFO - Automação finalizada."
    ]
    log_area.insert(tk.END, "\n".join(logs))
    log_area.config(state='disabled')

    # --- Lado Direito: Botões e Notificações ---
    frame_direita = tk.Frame(frame)
    frame_direita.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    frame_direita.columnconfigure(0, weight=1)

    def exportar_logs():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write("\n".join(logs))
            messagebox.showinfo("Exportar Logs", "Logs exportados com sucesso!")

    frame_botoes = tk.Frame(frame_direita)
    frame_botoes.grid(row=0, column=0, pady=5)

    tk.Button(frame_botoes, text="Atualizar", width=15,
              command=lambda: messagebox.showinfo("Atualizar", "Logs atualizados!")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes, text="Exportar Logs", width=15,
              command=exportar_logs).pack(side=tk.LEFT, padx=5)

    tk.Label(frame_direita, text="Notificações", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", pady=10)

    notificacoes_area = scrolledtext.ScrolledText(frame_direita, width=45, height=7, state='normal')
    notificacoes_area.grid(row=2, column=0, sticky="nsew", pady=5)
    notificacoes_area.insert(tk.END, "Nenhuma notificação no momento.\n")
    notificacoes_area.config(state='disabled')
