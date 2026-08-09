from tkinter import *
from tkinter import ttk

class Formatacao:
    def validar_formatar_data(self, data):
        try:
            dia, mes, ano = data.split('/')
            if len(ano) == 4:
                return f"{ano}-{mes}-{dia}"
            else:
                raise ValueError("Ano com formato inválido")
        except Exception as e:
            raise ValueError(f"Data em formato inválido. Use DD/MM/YYYY. Erro: {e}")     

    def formatar_data(self, entry, event):
        texto = entry.get().replace("/", "")[:8]    
        novotexto = ""
        if event.keysym.lower() == "backspace":
            return
        for x in range(len(texto)):
            if not texto[x].isdigit():
                continue
            if x in [1, 3]:
                novotexto += texto[x] + "/"
            else:
                novotexto += texto[x]
        entry.delete(0, "end")
        entry.insert(0, novotexto)

    def formatar_cpf(self, entry, event):
        texto = entry.get().replace(".", "").replace("-", "")[:11]    
        novotexto = ""
        if event.keysym.lower() == "backspace":
            return
        for x in range(len(texto)):
            if not texto[x].isdigit():
                continue
            if x in [2, 5]:
                novotexto += texto[x] + "."
            elif x == 8:
                novotexto += texto[x] + "-"
            else:
                novotexto += texto[x]
        entry.delete(0, "end")
        entry.insert(0, novotexto) 

    def formatar_horario(self, entry, event):
        texto = entry.get().replace(":", "")[:4]    
        novotexto = ""
        if event.keysym.lower() == "backspace":
            return
        for x in range(len(texto)):
            if not texto[x].isdigit():
                continue
            if x == 1:
                novotexto += texto[x] + ":"
            else:
                novotexto += texto[x]
        entry.delete(0, "end")
        entry.insert(0, novotexto)

    def formatar_telefone(self, entry, event):
        texto = entry.get().replace("(", "")[:14]    
        novotexto = "("
        if event.keysym.lower() == "backspace":
            return
        for x in range(len(texto)):
            if not texto[x].isdigit():
                continue
            if x in [1,2]:
                novotexto += texto[x] + ") "
            elif x == 8: 
                novotexto += texto[x] + "-"
            else: 
                novotexto += texto[x]
        entry.delete(0, "end")
        entry.insert(0, novotexto)
    
    def formatar_cedula(self, entry, event): 
        texto = entry.get().replace(",", "").replace(".", "") 
        if texto.isdigit():  
            valor = int(texto) / 100  
            entry.delete(0, "end")  
            entry.insert(0, f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    def limpar_todos_campos(self, container):
        for widget in container.winfo_children():
            if isinstance(widget, (Entry, ttk.Combobox)):
                widget.delete(0, END)
            elif isinstance(widget, (Frame, LabelFrame)):
                self.limpar_todos_campos(widget)
