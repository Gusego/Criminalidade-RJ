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
contagem_crimes = df_rj['evento'].value_counts()

# Interface de visualização de dados
def mostrar_interface():
    root = tk.Tk()
    root.title("Criminalidade - Município do Rio de Janeiro")
    root.state("zoomed")  # Janela cheia
    root.configure(bg="#2C3E50")  # Azul escuro sofisticado

    style = ttk.Style()
    style.configure("TFrame", background="#2C3E50")
    style.configure("TLabel", background="#ffffff", font=("Arial", 16, "bold"))
    style.configure("TButton", font=("Arial", 12), padding=10)

    content = ttk.Frame(root, padding=20)
    content.pack(expand=True)

    # Gráfico maior
    graph_frame = ttk.Frame(content)
    graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    fig, ax = plt.subplots(figsize=(20, 12))  
    contagem_crimes.head(10).plot(kind='barh', ax=ax, color='mediumpurple')

    ax.set_title("Top 10 Crimes no Município do RJ", fontsize=16)  
    ax.set_xlabel("Quantidade", fontsize=14)
    ax.set_ylabel("Tipo de Crime", fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)  
    fig.tight_layout(pad=3)

    canvas_graph = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas_graph.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    canvas_graph.draw()

    btn_sair = ttk.Button(content, text="Fechar", command=root.destroy)
    btn_sair.pack(pady=20)

    root.mainloop()

# Menu principal
def main_menu():
    root = tk.Tk()
    root.title("Sistema de Criminalidade RJ")
    root.geometry("400x250")
    root.configure(bg="#2C3E50")  # Azul escuro sofisticado

    style = ttk.Style()
    style.configure("TFrame", background="#2C3E50")
    style.configure("TLabel", background="#ffffff", font=("Arial", 16, "bold"))
    style.configure("TButton", font=("Arial", 12), padding=10)

    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)

    lbl_titulo = ttk.Label(frame, text="Sistema de Criminalidade RJ")
    lbl_titulo.pack(pady=10)

    btn_dados = ttk.Button(frame, text="📊 Dados Município RJ", command=mostrar_interface)
    btn_dados.pack(pady=10)

    btn_sair = ttk.Button(frame, text="❌ Sair", command=root.destroy)
    btn_sair.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
