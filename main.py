import sys
import subprocess
import tkinter as tk
from tkinter import ttk

def abrir_trabalhobigdata():
    # Executa o script com o mesmo interpretador Python do menu
    subprocess.Popen([sys.executable, 'trabalhobigdata.py'])

def main_menu():
    root = tk.Tk()
    root.title("Menu Inicial")
    root.geometry("300x150")

    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)

    btn_dados = ttk.Button(frame, text="Dados município RJ", command=abrir_trabalhobigdata)
    btn_dados.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
