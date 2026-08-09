from tkinter import *
from tkinter import ttk, filedialog
from reportlab.pdfgen import canvas
import os
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from utils.formatacao import Formatacao
from config import pastaApp

class Financeiro:
    def __init__(self,root_pai):
        self.banco=BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()

        self.toplevel = Toplevel(root_pai)
        self.toplevel.overrideredirect(True)
        self.toplevel.configure(background="#f5f6fa")
        self.centralizador.centralizar_toplevel(self.toplevel, 700, 380, root_pai)

        self.frame_1=Frame(self.toplevel,relief="sunken",background="#2F3542")
        self.frame_1.place(x=-1,y=-1,width=899,height=82)

        self.label_1=Label(self.toplevel,text="FINANCEIRO",background="#2F3542",font=("arial",20,"bold"),fg="white")
        self.label_1.place(x=250,y=30,width=200,height=30) 

        self.botao_clientes=Button(self.toplevel,relief="flat",borderwidth=2,font=("arial 10 bold"),text="             FINANCEIRO CLIENTES [F1]",background="#9a9898",foreground="white",anchor="center",activebackground="#9a9898", cursor="hand2",command=self.financeiro_clientes)
        self.botao_clientes.place(x=100,y=160,width=265,height=100)
        self.imagem_logo_2=PhotoImage(file=pastaApp+"\\IMG\\Refund1.png")
        self.label_logo=Label(self.toplevel,image=self.imagem_logo_2,background="#9a9898")
        self.label_logo.place(x=105,y=180)
        
        self.botao_contas_receber=Button(self.toplevel,relief="flat",borderwidth=2,font=("arial 10 bold"),text="              CONTAS A RECEBER [F2]",background="#9a9898",foreground="white",anchor="center",activebackground="#9a9898", cursor="hand2",command=self.financeiro_contas_receber)
        self.botao_contas_receber.place(x=390,y=160,width=265,height=100)
        self.imagem_logo_3=PhotoImage(file=pastaApp+"\\IMG\\Money.png")
        self.label_logo=Label(self.toplevel,image=self.imagem_logo_3,background="#9a9898")
        self.label_logo.place(x=400,y=176)

        btn_close = Button(self.toplevel, text="X", bg="red", fg="white", cursor="hand2",command=self.toplevel.destroy, bd=0)
        btn_close.place(x=670, y=5, width=25, height=20)

        self.toplevel.wait_window()
    
    def cancelar(self):
        self.toplevel.destroy()

    def financeiro_contas_receber(self):
        FinanceiroContasReceber(self.toplevel)
      
    def financeiro_clientes(self):
        FinanceiroClientes(self.toplevel)

class FinanceiroContasReceber:
    def __init__(self,root_pai):
        self.banco=BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()
        self.formatacao=Formatacao()
        self.toplevel = Toplevel(root_pai)
        self.centralizador.centralizar_toplevel(self.toplevel, 800, 400, root_pai)
        
        self.frame_1=Frame(self.toplevel,relief="sunken", background="#e0e0e0")
        self.frame_1.place(x=-1,y=-1,width=802,height=70)

        self.label_1=Label(self.toplevel,text="CONTAS A RECEBER", background="#e0e0e0",font=("arial",18,"bold"),fg="black")
        self.label_1.place(x=280,y=30,width=290,height=30)

        self.frame_1=LabelFrame(self.toplevel,text="Dados do Lançamento",background="#e0e0e0",font=("candara",10,"italic"))
        self.frame_1.place(x=15,y=75,width=770,height=240)

        self.label_nome=Label(self.toplevel,text="CLIENTE",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_nome.place(x=23,y=90,width=55,height=20)
        self.entry_nome=Entry(self.toplevel,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_nome.place(x=22,y=110,width=460,height=30)
        self.entry_nome.focus()
 
        self.label_cpf=Label(self.toplevel,text="CPF",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_cpf.place(x=505,y=90,width=40,height=20)
        self.entry_cpf=Entry(self.toplevel,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_cpf.bind("<KeyRelease>", lambda e: self.formatacao.formatar_cpf(self.entry_cpf, e))
        self.entry_cpf.place(x=510,y=110,width=260,height=30)

        self.label_data_emissao=Label(self.toplevel,text="DATA EMISSÃO",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_data_emissao.place(x=23,y=140,width=100,height=20)
        self.entry_data_emissao=Entry(self.toplevel,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_data_emissao.bind("<KeyRelease>", lambda e: self.formatacao.formatar_data(self.entry_data_emissao, e))
        self.entry_data_emissao.place(x=23,y=160,width=160,height=30)

        self.label_data_pagamento=Label(self.toplevel,text="VENCIMENTO",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_data_pagamento.place(x=190,y=140,width=100,height=20)
        self.entry_data_pagamento=Entry(self.toplevel,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_data_pagamento.bind("<KeyRelease>", lambda e: self.formatacao.formatar_data(self.entry_data_pagamento, e))
        self.entry_data_pagamento.place(x=195,y=160,width=160,height=30) 

        self.label_referente=Label(self.toplevel,text="REFERENTE",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_referente.place(x=355,y=140,width=110,height=20)
        self.combobox_2=ttk.Combobox(self.toplevel,font=("calibri",15),values=["exame:covid-19","exame:sangue","exame:urina"])
        self.combobox_2.place(x=370,y=160,width=400,height=30)
        self.combobox_2.set("")
    
        self.label_valor_pago=Label(self.toplevel,text="VALOR PAGO (R$)",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_valor_pago.place(x=21,y=190,width=120,height=20)
        self.entry_valor_pago=Entry(self.toplevel,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_valor_pago.bind("<KeyRelease>", lambda e: self.formatacao.formatar_cedula(self.entry_valor_pago, e))
        self.entry_valor_pago.place(x=22,y=210,width=180,height=30)
        
        self.label_valor_receber=Label(self.toplevel,text="VALOR A RECEBER (R$)",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_valor_receber.place(x=440,y=190,width=150,height=20)
        self.entry_valor_receber=Entry(self.toplevel,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_valor_receber.bind("<KeyRelease>", lambda e: self.formatacao.formatar_cedula(self.entry_valor_receber, e))
        self.entry_valor_receber.place(x=440,y=210,width=150,height=30)
        
        self.label_status=Label(self.toplevel,text="STATUS PAGAMENTO (R$)",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_status.place(x=601,y=190,width=165,height=20)
        self.combobox_1 = ttk.Combobox(self.toplevel,font=("calibri",15),values=["EFETUADO", "A RECEBER"])
        self.combobox_1.place(x=600,y=210,width=170,height=30)
        self.combobox_1.set("")

        self.botao_cancelar=Button(self.toplevel,text="      FECHAR [F2]",relief="flat",background="#9a9898",foreground="white",font=("arial",10,"bold"),activebackground="#D3D3D3",activeforeground="black", cursor="hand2",command=self.cancelar)
        self.botao_cancelar.place(x=403,y=360,width=120,height=32)
        self.imagem_logo_2=PhotoImage(file=pastaApp+"\\IMG\\x.png")
        self.label_logo_1=Label(self.toplevel,image=self.imagem_logo_2,background="#9a9898")
        self.label_logo_1.place(x=405,y=363)
                
        self.botao_salvar=Button(self.toplevel,text="    SALVAR [F1]",relief="flat",background="#9a9898",foreground="white",font=("arial",10,"bold"),activebackground="#D3D3D3",activeforeground="black", cursor="hand2",command=self.salvar)
        self.botao_salvar.place(x=278,y=360,width=120,height=32)
        self.imagem_logo_1=PhotoImage(file=pastaApp+"\\IMG\\save.png")
        self.label_logo=Label(self.toplevel,image=self.imagem_logo_1,background="#9a9898")
        self.label_logo.place(x=280,y=362)

        self.toplevel.wait_window()
    
    def cancelar(self):
        resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja fechar a janela?", cor_fundo="#A9A9A9", cor_texto="black")
        if resposta:
            self.toplevel.destroy()
        else:
            self.entry_nome.focus()
    
    def salvar(self):
        self.banco.conectar()
        nome=self.entry_nome.get().strip()
        cpf=self.entry_cpf.get().strip()
        data_emissao=self.entry_data_emissao.get().strip()
        vencimento=self.entry_data_pagamento.get().strip()
        referente=self.combobox_2.get().strip()
        valor_pago=self.entry_valor_pago.get().strip()
        valor_receber=self.entry_valor_receber.get().strip()
        status=self.combobox_1.get().strip()
        if nome=="":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Digite todos os campos!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return 
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja incluir no sistema?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql= "INSERT INTO sys_lab_contasreceber (nome,cpf,data_emissao,vencimento,referente,valor_pago,valor_receber,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                valores_sql=(nome, cpf, data_emissao, vencimento, referente, valor_pago, valor_receber, status)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem", texto="Dados inseridos!", cor_fundo="#A9A9A9", cor_texto="black", caminho_img="IMG/sucesso.png")
                self.formatacao.limpar_todos_campos(self.toplevel)
                self.entry_nome.focus()    
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao inserir....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()    

class FinanceiroClientes:
    def __init__(self,root_pai):
        self.banco=BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()
        self.formatacao=Formatacao()

        self.root_pai= root_pai
        self.toplevel = Toplevel(root_pai)
        self.toplevel.grab_set()
        self.toplevel.title("")
        self.toplevel.geometry("1122x506")
        self.toplevel.iconbitmap('IMG\\iconeprograma.ico')
        self.toplevel.configure(background="black",border=1,relief="solid")
        self.toplevel.resizable(False, False)
        self.toplevel.transient(self.root_pai)
        self.centralizador.centralizar_toplevel(self.toplevel, 1122, 506, root_pai)

        frame_tree = ttk.Frame(self.toplevel)
        frame_tree.place(x=1, y=100, width=1118, height=403)

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading",font=("Segoe UI", 11, "bold"),background="#E6EFF9",foreground="black",borderwidth=0)
        self.style.configure("Treeview",font=("Segoe UI", 10, "bold"),background="#C6E2FF",foreground="#070707",rowheight=32,fieldbackground="#B4CDCD")
        self.style.map("Treeview",background=[("selected", "#4a7efc")],foreground=[("selected", "#ffffff")])

        self.scrollbar = ttk.Scrollbar(frame_tree, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)
    
        self.tree_view=ttk.Treeview(frame_tree,columns=('nome','cpf','emissao','vencimento','referente','valor pago','valor a receber','status'),show="headings", yscrollcommand=self.scrollbar.set)
        self.tree_view.column('nome', minwidth=0, width=110)
        self.tree_view.column('cpf', minwidth=0, width=70)    
        self.tree_view.column('emissao', minwidth=0, width=80)
        self.tree_view.column('vencimento', minwidth=0, width=80)
        self.tree_view.column('referente', minwidth=0, width=150)
        self.tree_view.column('valor pago', minwidth=0, width=90)
        self.tree_view.column('valor a receber', minwidth=0, width=102)
        self.tree_view.column('status', minwidth=0, width=50)
        self.tree_view.heading('nome',text="👤 NOME",anchor=W)
        self.tree_view.heading('cpf',text="CPF",anchor=W)
        self.tree_view.heading('emissao',text="📅 EMISSAO",anchor=W)
        self.tree_view.heading('vencimento',text="VENCIMENTO",anchor=W)
        self.tree_view.heading('referente',text="🧪 REFERENTE",anchor=W)
        self.tree_view.heading('valor pago',text="💰 VALOR PAGO ",anchor=W)
        self.tree_view.heading('valor a receber',text="VALOR A RECEBER",anchor=W)
        self.tree_view.heading('status',text="⚠️ STATUS",anchor=W)  
        self.tree_view.tag_configure("pago", foreground="#2da64a")      
        self.tree_view.tag_configure("pendente", foreground="#fc3142")

        self.scrollbar.config(command=self.tree_view.yview)
        self.tree_view.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree_view.bind("<Double-1>", self.janela_pesquisa)

        self.item_selecionado = False

        self.banco.conectar()
        self.tree_view.delete(*self.tree_view.get_children())
        codigo_sql = 'SELECT * FROM sys_lab_contasreceber'
        self.banco.cursor.execute(codigo_sql)
        resultado_sql = self.banco.cursor.fetchall()
        for i, f in enumerate(resultado_sql):
            status = f[8]
            tag_status = self.definir_status_tag(status)
            tag_zebra = "par" if i % 2 == 0 else "impar"
            self.tree_view.insert("","end",id=f[0],text=f[0],values=(f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8]),tags=(tag_status,tag_zebra)
            )

        self.frame_1=Frame(self.toplevel,relief="sunken",border=1,background="#1E3D5F")
        self.frame_1.place(x=-1,y=-1,width=1124,height=100)

        self.label_1=Label(self.toplevel,text="FINANCEIRO CLIENTES", background="#1E3D5F", font=("arial",15,"bold"),fg="white")
        self.label_1.place(x=400,y=25,width=350,height=30)
    
        self.entry_nome_cliente = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_nome_cliente.place(x=1, y=68, width=230, height=30)
        self.entry_nome_cliente.insert(0, "Buscar....")
        self.entry_nome_cliente.config(fg="gray")

        self.botao_consulta_paciente=Button(self.toplevel,relief="flat",borderwidth=2,font=("arial 9 bold"),text="       PESQUISAR CLIENTE [F1]",background="#4a7efc",foreground="white",anchor="center",activebackground="#4a7efc", activeforeground="white", cursor="hand2", command=self.check_input)
        self.botao_consulta_paciente.place(x=232,y=68,width=196,height=30)
        self.imagem_logo_5=PhotoImage(file=pastaApp+"\\IMG\\icon3.png")
        self.label_logo=Label(self.toplevel,image=self.imagem_logo_5,background="#4a7efc")
        self.label_logo.place(x=233,y=69) 

        self.entry_nome_cliente.bind("<FocusIn>", self.entry_on)
        self.entry_nome_cliente.bind("<FocusOut>", self.entry_of)

    def cancelar(self):
        self.toplevel.destroy()

    def entry_on(self, event):
        if  self.entry_nome_cliente.get() == "Buscar....":
                self.entry_nome_cliente.delete(0, "end")
                self.entry_nome_cliente.config(fg="black")

    def entry_of(self, event):
        if  self.entry_nome_cliente.get() == "":
                self.entry_nome_cliente.insert(0, "Buscar....")
                self.entry_nome_cliente.config(fg="gray")
    
    def definir_status_tag(self,status):
        status = status.strip().upper()

        if status == "EFETUADO":
            return "pago"
        elif status == "A RECEBER":
            return "pendente"
        else:
            return ""
        
    def janela_pesquisa(self, event):
        item = self.tree_view.focus()
        if not item:
            return

        valores = self.tree_view.item(item, "values")

        self.janela_edicao = Toplevel(self.toplevel)
        self.janela_edicao.geometry("700x330")
        self.janela_edicao.iconbitmap('IMG\\iconeprograma.ico')
        self.janela_edicao.configure(background="#e0e0e0")
        self.janela_edicao.transient(self.toplevel)
        self.janela_edicao.grab_set()
        self.janela_edicao.resizable(False, False)
        self.janela_edicao.title("")
        central = CentralizadorDeJanelas()
        central.centralizar_toplevel(self.janela_edicao, 700, 330, self.toplevel)

        frame = LabelFrame(self.janela_edicao,text="Editar Financeiro",background="#e0e0e0", foreground="black",borderwidth=1,relief="solid",font=("candara", 10, "italic"))
        frame.place(x=10, y=5, width=680, height=319)
        
        frame_borda_status = Frame(frame,bg="black")
        frame_borda_status.place(x=529, y=34, width=132, height=32) 

        self.label_nome = Label(frame, text="NOME", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_nome.place(x=10, y=15)
        self.entry_nome = Entry(frame, font=("calibri", 14), relief="solid", borderwidth=1)
        self.entry_nome.place(x=10, y=35, width=210, height=30)
        self.entry_nome.insert(0, valores[0])

        self.label_cpf = Label(frame, text="CPF", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_cpf.place(x=235, y=15)
        self.entry_cpf = Entry(frame, font=("calibri", 14), relief="solid", borderwidth=1)
        self.entry_cpf.place(x=235, y=35, width=140, height=30)
        self.entry_cpf.bind("<KeyRelease>", lambda e:self.formatacao.formatar_cpf(self.entry_cpf, e))
        self.entry_cpf.insert(0, valores[1])

        self.label_data_emissao = Label(frame, text="DATA EMISSÃO", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_data_emissao.place(x=390, y=15)
        self.entry_data_emissao = Entry(frame, font=("calibri", 14), relief="solid")
        self.entry_data_emissao.place(x=390, y=35, width=130, height=30)
        self.entry_data_emissao.bind("<KeyRelease>", lambda e:self.formatacao.formatar_data(self.entry_data_emissao, e))
        self.entry_data_emissao.insert(0, valores[2])

        self.label_data_pagamento = Label(frame, text="VENCIMENTO", bg="#e0e0e0", fg="black", font=("arial", 10, "bold"))
        self.label_data_pagamento.place(x=10, y=80)
        self.entry_data_pagamento = Entry(frame, font=("calibri", 14), relief="solid")
        self.entry_data_pagamento.place(x=10, y=100, width=150, height=30)
        self.entry_data_pagamento.bind("<KeyRelease>", lambda e:self.formatacao.formatar_data(self.entry_data_pagamento, e))
        self.entry_data_pagamento.insert(0, valores[3])

        self.label_referente = Label(frame, text="REFERENTE", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_referente.place(x=170, y=80)
        self.entry_referente = Entry(frame, font=("calibri", 14), relief="solid")
        self.entry_referente.place(x=170, y=100, width=200, height=30)
        self.entry_referente.insert(0, valores[4])

        self.label_valor_pago = Label(frame, text="VALOR PAGO", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_valor_pago.place(x=380, y=80)
        self.entry_valor_pago = Entry(frame, font=("calibri", 14), relief="solid")
        self.entry_valor_pago.place(x=380, y=100, width=130, height=30)
        self.entry_valor_pago.bind("<KeyRelease>", lambda e:self.formatacao.formatar_cedula(self.entry_valor_pago, e))
        self.entry_valor_pago.insert(0, valores[5])

        self.label_valor_receber = Label(frame, text="VALOR REC.", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_valor_receber.place(x=520, y=80)
        self.entry_valor_receber = Entry(frame, font=("calibri", 14), relief="solid")
        self.entry_valor_receber.place(x=520, y=100, width=140, height=30)
        self.entry_valor_receber.bind("<KeyRelease>", lambda e:self.formatacao.formatar_cedula(self.entry_valor_receber, e))
        self.entry_valor_receber.insert(0, valores[6])

        self.label_status = Label(frame, text="STATUS", bg="#e0e0e0",fg="black", font=("arial", 10, "bold"))
        self.label_status.place(x=532, y=14, width=50, height=17)
        self.combobox_1 = ttk.Combobox(frame, font=("calibri", 12),values=["EFETUADO", "A RECEBER"], background="silver")
        self.combobox_1.place(x=530, y=35, width=130, height=30)
        self.combobox_1.set(valores[7])

        self.botao_atualizar = Button(frame,relief="solid",borderwidth=1,font=("arial", 10, "bold"),text="    ATUALIZAR [F1]",background="#E8F0F1",foreground="black",command=self.atualizar_cliente)
        self.botao_atualizar.place(x=100, y=220, width=150, height=40)
        self.imgLogo3=PhotoImage(file=pastaApp+"\\IMG\\icon4.png")
        self.l_logo=Label(frame,image=self.imgLogo3,background="#E8F0F1")
        self.l_logo.place(x=102,y=225)

        self.botao_excluir = Button(frame,relief="solid",borderwidth=1,font=("arial", 10, "bold"),text="    EXCLUIR [F2]",background="#E8F0F1",foreground="black",command=self.excluir_cliente)
        self.botao_excluir.place(x=255, y=220, width=150, height=40)
        self.imgLogo2=PhotoImage(file=pastaApp+"\\IMG\\icon2.png")
        self.l_logo=Label(frame,image=self.imgLogo2,background="#E8F0F1")
        self.l_logo.place(x=257,y=225)   


        self.botao_pdf = Button(frame,relief="solid",borderwidth=1,font=("arial", 10, "bold"),text="     RECIBO [F3]",background="#E8F0F1",foreground="black",command=self.criar_pdf)
        self.botao_pdf.place(x=409, y=220, width=150, height=40)
        self.imgLogo4=PhotoImage(file=pastaApp+"\\IMG\\imgpdf.png")
        self.l_logo=Label(frame,image=self.imgLogo4,background="#E8F0F1")
        self.l_logo.place(x=411,y=225)

        
    def criar_pdf(self):
        self.banco.conectar()
        nome_pdf = self.entry_nome.get().strip()
        cpf_pdf = self.entry_cpf.get().strip()
        valor_pago_pdf = self.entry_valor_pago.get().strip()
        referente_pdf = self.entry_referente.get().strip()
        if  nome_pdf == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Recibo não pode ser gerado\n por falta de informações!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return 
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("Arquivo PDF", "*.pdf")],title="Salvar relatório de exames")
        if not caminho_arquivo:
            return
        self.canvas = canvas.Canvas(caminho_arquivo)

        self.canvas.setFont("Helvetica",16)
        self.canvas.drawString(220,750,"Laboratorio São Bento")
        self.canvas.drawString(90,735,"Avenida marechal rondom, 1036, Vila Guaporé, Pontes e Lacerda MT")
        self.canvas.drawString(150,719,"Telefone 3266-4753, Whatsapp (65) 9 8121-7523")
        self.canvas.drawString(30,700,"____________________________________________________________")

        self.logo_width = 30
        self.logo_height = 30 
        self.canvas.drawImage("IMG/logo_pdf.png", 280, 770, self.logo_width, self.logo_height)

        self.canvas.setFont("Helvetica-Bold",20)
        self.canvas.drawString(50,592, 'RECIBO DE PAGAMENTO')
        self.canvas.drawString(450,592, 'R$ '+valor_pago_pdf)

        self.canvas.setFont("Helvetica",16)
        self.canvas.drawString(90,200,"________________________________________________")
        self.canvas.drawString(225,180,"Laboratorio São Bento")
    
        self.canvas.setFont("Helvetica", 16)
        texto_1 = f"Recebemos de {nome_pdf}, portador do cpf {cpf_pdf}, "
        self.canvas.drawString(70, 500, texto_1)
        texto_2 = f" a importância de R$ {valor_pago_pdf}, referente a {referente_pdf}"
        self.canvas.drawString(90, 486, texto_2)

        self.canvas.showPage()
        self.canvas.save()
        self.formatacao.limpar_todos_campos(self.toplevel)
        self.mensagem.alerta_erro_sucesso(titulo="Sucesso", texto="Recibo gerado com sucesso!", cor_fundo="#A9A9A9", caminho_img="IMG/sucesso.png")

        self.item_selecionado = False   
   
    def check_input(self):
        self.banco.conectar()
        nome_cliente = self.entry_nome_cliente.get().strip()
        if nome_cliente == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Informe o nome para pesquisa!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return
        try:
            #self.tree_view.delete(*self.tree_view.get_children())
            codigo_sql = "SELECT * FROM sys_lab_contasreceber WHERE nome LIKE %s ORDER BY id"
            valores_sql=('%' + nome_cliente + '%',)
            self.banco.cursor.execute(codigo_sql, valores_sql)
            resultado_sql = self.banco.cursor.fetchall()
            if  len(resultado_sql) > 0:
                for linha in resultado_sql:
                    self.tree_view.insert("", "end", values=(linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10]))
            else:
                self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Não foi localizado nenhum cliente!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
                self.entry_nome_cliente.delete(0,END)
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao selecionar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()

    def excluir_cliente(self):
        self.banco.conectar()
        cpf=self.entry_cpf.get().strip()
        if cpf =="":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Selecione um cliente para excluir!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja excluir o cliente?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql ='DELETE FROM sys_lab_contasreceber WHERE cpf = %s'
                valores_sql=(cpf,)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Sucesso", texto="Cliente Excluido!", cor_fundo="#A9A9A9", caminho_img="IMG/sucesso.png")
                self.tree_view.delete(*self.tree_view.get_children())
                self.formatacao.limpar_todos_campos(self.toplevel)
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao deletar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()
        
    def atualizar_cliente(self):
        self.banco.conectar()
        nome=self.entry_nome.get().strip()
        cpf=self.entry_cpf.get().strip()
        data_emissao=self.entry_data_emissao.get().strip()
        vencimento=self.entry_data_pagamento.get().strip()
        referente=self.entry_referente.get().strip()
        valor_pago=self.entry_valor_pago.get().strip()
        valor_receber=self.entry_valor_receber.get().strip()
        status=self.combobox_1.get().strip()
        if nome=="":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Selecione um cliente\n para realizar a ação!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return         
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja atualizar o cliente?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql ='UPDATE sys_lab_contasreceber SET nome = %s, cpf =%s, data_emissao =%s, vencimento =%s, referente =%s, valor_pago =%s, valor_receber =%s, status =%s WHERE cpf=%s'
                valores_sql=(nome, cpf, data_emissao, vencimento, referente, valor_pago, valor_receber, status, cpf)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem", texto="Dados atualizados!", cor_fundo="#A9A9A9", cor_texto="black", caminho_img="IMG/sucesso.png")
                self.tree_view.delete(*self.tree_view.get_children())
                self.formatacao.limpar_todos_campos(self.toplevel)
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao atualizar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()
    
