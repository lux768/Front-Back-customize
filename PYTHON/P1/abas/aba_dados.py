import tkinter as tk
from tkinter import filedialog

def criar_aba_dados(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Dados")

    tk.Label(frame, text="Relatórios Gerados", font=("Arial", 12)).pack(pady=5)
    tk.Label(frame, text="(Aqui você pode exibir gráficos, tabelas, etc.)").pack(pady=5)
    tk.Button(frame, text="Exportar para PDF/Excel", command=lambda: tk.messagebox.showinfo("Relatórios", "Relatório exportado.")).pack(pady=5)

    def upload_arquivo():
        file_path = filedialog.askopenfilename()
        if file_path:
            tk.messagebox.showinfo("Upload", f"Arquivo '{file_path}' selecionado.")

    def download_relatorio():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write("Exemplo de relatório gerado.")
            tk.messagebox.showinfo("Download", "Relatório salvo com sucesso.")

    tk.Label(frame, text="Upload de Arquivo", font=("Arial", 12)).pack(pady=5)
    tk.Button(frame, text="Selecionar Arquivo", command=upload_arquivo).pack(pady=2)
    tk.Label(frame, text="Download de Relatório", font=("Arial", 12)).pack(pady=10)
    tk.Button(frame, text="Baixar Relatório", command=download_relatorio).pack(pady=2)
