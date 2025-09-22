import tkinter as tk
from tkinter import messagebox

def iniciar_automacao():
    status_var.set("Status: Executando...")
    # Aqui você pode chamar sua função de automação
    messagebox.showinfo("Automação", "Automação iniciada!")

def ver_relatorios():
    messagebox.showinfo("Relatórios", "Aqui você verá os relatórios.")

def abrir_configuracoes():
    messagebox.showinfo("Configurações", "Aqui você ajusta as configurações.")

def sair():
    root.destroy()

root = tk.Tk()
root.title("Dashboard - Automação Python")
root.geometry("400x300")

tk.Label(root, text="Bem-vindo à Automação Python!", font=("Arial", 16)).pack(pady=10)

status_var = tk.StringVar(value="Status: Pronto")
tk.Label(root, textvariable=status_var, fg="green").pack(pady=5)

tk.Button(root, text="Iniciar Automação", width=20, command=iniciar_automacao).pack(pady=5)
tk.Button(root, text="Ver Relatórios", width=20, command=ver_relatorios).pack(pady=5)
tk.Button(root, text="Configurações", width=20, command=abrir_configuracoes).pack(pady=5)
tk.Button(root, text="Sair", width=20, command=sair).pack(pady=20)

root.mainloop()
