from tkinter import *
from tkinter import ttk

AZUL_HEADER = "#1f3d5a"
AZUL_TREE = "#274e73"
FUNDO_TELA = "#5f7d99"
BRANCO = "#ffffff"

class TelaResultados:
    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.title("SYS LAB - Resultados")
        self.top.geometry("1000x600")
        self.top.configure(bg=FUNDO_TELA)
    
        header = Frame(self.top, bg=AZUL_HEADER, height=50)
        header.pack(fill="x")

        Label(header,text="RESULTADOS DE EXAMES",font=("Arial", 14, "bold"),bg=AZUL_HEADER,fg="white").pack(side="left", padx=15)

        Button(header,text="✖",bg=AZUL_HEADER,fg="white",relief="flat",command=self.top.destroy,cursor="hand2").pack(side="right", padx=10)
        
        frame_busca = Frame(self.top, bg=FUNDO_TELA)
        frame_busca.pack(fill="x", padx=10, pady=8)

        self.entry_buscar = Entry(frame_busca, font=("Arial", 10))
        self.entry_buscar.pack(side="left", fill="x", expand=True, padx=(0, 10))

        Button(frame_busca,text="🔍 PESQUISAR [F1]",bg="#2f66ff",fg="white",relief="flat",cursor="hand2").pack(side="left")
        
        frame_tree = Frame(self.top, bg=FUNDO_TELA)
        frame_tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        colunas = ("paciente", "exame", "valor", "unidade", "data")

        self.tree = ttk.Treeview(frame_tree,columns=colunas,show="headings")

        for col in colunas:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_tree,orient="vertical",command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.tag_configure("par", background="#e6edf5")
        self.tree.tag_configure("impar", background="#ffffff")
