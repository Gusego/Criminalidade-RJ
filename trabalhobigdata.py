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


def mostrar_interface():
    root = tk.Tk()
    root.title("Criminalidade - Município do Rio de Janeiro")
    root.state("zoomed")  # Janela cheia

    root.configure(bg="#f0f0f0")

    style = ttk.Style()
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", font=("Arial", 14))
    style.configure("TButton", font=("Arial", 12), padding=6)

    # Canvas principal com scrollbar
    canvas = tk.Canvas(root, bg="#f0f0f0", highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_configure)

    # Conteúdo centralizado com largura máxima
    content = ttk.Frame(scrollable_frame, width=1100)
    content.pack(anchor="n", pady=20)

    # Texto com scrollbar
    text_frame = ttk.Frame(content)
    text_frame.pack(fill=tk.BOTH, expand=False, pady=10)

    scroll_y = tk.Scrollbar(text_frame, orient=tk.VERTICAL)
    txt = tk.Text(text_frame, height=15, wrap=tk.WORD, yscrollcommand=scroll_y.set,
                  font=("Consolas", 11), background="#ffffff", foreground="#333333")
    scroll_y.config(command=txt.yview)

    txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    txt.insert(tk.END, contagem_crimes.to_string())
    txt.config(state=tk.DISABLED)

    # Gráfico com redimensionamento
    graph_frame = ttk.Frame(content)
    graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    fig, ax = plt.subplots(figsize=(10, 5))
    contagem_crimes.head(10).plot(kind='bar', ax=ax, color='mediumpurple')
    ax.set_title("Top 10 Crimes no Município do RJ")
    ax.set_ylabel("Quantidade")
    ax.set_xlabel("Tipo de Crime")

    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout(pad=3)  # Ajusta espaçamento para não cortar texto

    canvas_graph = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas_graph.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)  # Agora redimensiona com a janela
    canvas_graph.draw()

    lbl = ttk.Label(content, text="Todos os tipos de crimes no Município do RJ", font=("Arial", 16, "bold"))
    lbl.pack(pady=10)

    
    # Botão de sair
    btn_sair = ttk.Button(content, text="Fechar", command=root.destroy)
    btn_sair.pack(pady=20)

    root.mainloop()


mostrar_interface()
