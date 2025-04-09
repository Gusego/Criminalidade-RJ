# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 19:04:20 2025

@author: Gustavo
"""
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Lê o arquivo CSV
df = pd.read_csv("BancoVDE 2025.csv", sep=",", encoding="latin1")

# Padroniza os nomes das colunas e dados
df.columns = df.columns.str.lower().str.strip()
df['municipio'] = df['municipio'].str.upper().str.strip()
df['evento'] = df['evento'].str.strip()

# Filtra apenas o município do Rio de Janeiro
df_rj = df[(df['uf'] == 'RJ') & (df['municipio'] == 'RIO DE JANEIRO')]

# Conta todas as ocorrências por tipo de crime
contagem_crimes = df_rj['evento'].value_counts()

# Cria a interface gráfica
def mostrar_interface():
    root = tk.Tk()
    root.title("Criminalidade - Município do Rio de Janeiro")
    root.geometry("900x700")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    lbl = ttk.Label(frame, text="Todos os tipos de crimes no Município do RJ", font=("Arial", 14))
    lbl.pack(pady=10)

    txt = tk.Text(frame, height=15)
    txt.pack(fill=tk.X, expand=False)
    txt.insert(tk.END, contagem_crimes.to_string())

    # Exibe os 10 crimes mais comuns em gráfico
    fig, ax = plt.subplots(figsize=(8, 4))
    contagem_crimes.head(10).plot(kind='bar', ax=ax, color='purple')
    ax.set_title("Top 10 Crimes no Município do RJ")
    ax.set_ylabel("Quantidade")
    ax.set_xlabel("Tipo de Crime")
    plt.xticks(rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    root.mainloop()

mostrar_interface()
