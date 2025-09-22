import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def abrir_tela_logs(root, abrir_tela_inicial):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Logs da Automação", font=("Arial", 14)).pack(pady=10)

    log_area = scrolledtext.ScrolledText(root, width=60, height=15, state='normal')
    log_area.pack(padx=10, pady=10)
    logs = [
        "2025-09-22 10:00:01 - INFO - Automação iniciada.",
        "2025-09-22 10:00:05 - SUCCESS - Processamento concluído.",
        "2025-09-22 10:01:10 - ERROR - Falha ao acessar arquivo.",
        "2025-09-22 10:02:00 - INFO - Automação finalizada."
    ]
    log_area.insert(tk.END, "\n".join(logs))
    log_area.config(state='disabled')

    def exportar_logs():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write("\n".join(logs))
            messagebox.showinfo("Exportar Logs", "Logs exportados com sucesso!")

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10)

    tk.Button(frame_botoes, text="Atualizar", width=15, command=lambda: messagebox.showinfo("Atualizar", "Logs atualizados!")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes, text="Exportar Logs", width=15, command=exportar_logs).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botoes, text="Voltar", width=15, command=lambda: abrir_tela_inicial(root, abrir_tela_logs)).pack(side=tk.LEFT, padx=5)
