import tkinter as tk

def criar_aba_relatorios(notebook):
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Relatórios")

    tk.Label(frame, text="Relatórios Gerados", font=("Arial", 12)).pack(pady=5)
    tk.Label(frame, text="(Aqui você pode exibir gráficos, tabelas, etc.)").pack(pady=5)
    tk.Button(frame, text="Exportar para PDF/Excel", command=lambda: tk.messagebox.showinfo("Relatórios", "Relatório exportado.")).pack(pady=5)
