from tkinter import *
from datetime import datetime
from time import strftime
from config import pastaApp
from utils.banco import BancoDeDados
from utils.mensagem import CaixaMensagemPersonalizada
from telas.cadastro_clientes import CadastroDeClientes
from telas.agenda_consulta import AgendaConsulta
from telas.exames import Exames
from telas.editar_cadastro import EditarCadastroDeClientes
from telas.estoque import JanelaEstoque
from telas.financeiro import Financeiro
from telas.tela_resultados import TelaResultados

class TelaPrincipal:
    def __init__(self, root_original):#usuario
        self.banco=BancoDeDados()
        self.mensagem=CaixaMensagemPersonalizada() 
        
        self.root_original = root_original
        self.root = Toplevel(self.root_original)
        self.root.iconbitmap(pastaApp + "\\IMG\\iconeprograma.ico")
        self.root.title("SysLab - SOFTWARE PARA LABORATÓRIOS - VERSÃO 1.0")
        self.root.state('zoomed')
        self.root.configure(background="white")
        self.root.protocol("WM_DELETE_WINDOW", self.nao_fechar)

        #Teclas de atalho usadas no teclado.
        self.root.bind("<F1>", self.tecla_cadastro)
        self.root.bind("<F2>", self.tecla_agenda)
        self.root.bind("<F3>", self.tecla_estoque)
        self.root.bind("<F4>", self.tecla_exames)
        self.root.bind("<F5>", self.tecla_editarcadastro)
        self.root.bind("<F6>", self.tecla_financeiro) 
        self.root.bind("<F7>", self.tecla_sair)

        # BARRA DE MENU
        self.barrademenu = Menu(root_original)

        # MENU CADASTRO 
        self.filemenu = Menu(self.barrademenu, tearoff=0)
        self.filemenu.add_command(label="Cadastrar cliente", command=self.janela_cadastrocliente)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Sair", command=root_original.quit)
        self.barrademenu.add_cascade(label="Cadastro", menu=self.filemenu)

        # MENU EDITAR
        self.filemenu1 = Menu(self.barrademenu, tearoff=0)
        self.filemenu1.add_command(label="Editar Cadastro", command=self.janela_editar_cadastro)
        self.barrademenu.add_cascade(label="Editar", menu=self.filemenu1)

        # MENU EXAMES
        self.filemenu2 = Menu(self.barrademenu, tearoff=0)
        self.filemenu2.add_command(label="Exames", command=self.janela_exames)
        self.barrademenu.add_cascade(label="Exames", menu=self.filemenu2)

        # MENU ESTOQUE
        self.filemenu3 = Menu(self.barrademenu, tearoff=0)
        self.filemenu3.add_command(label=" Tela de estoque", command=self.janela_estoque)
        self.barrademenu.add_cascade(label="Estoque", menu=self.filemenu3)

        # MENU FINANCEIRO 
        self.filemenu4 = Menu(self.barrademenu, tearoff=0)
        self.filemenu4.add_command(label="Tela Financeiro", command=self.janela_financeiro)
        self.barrademenu.add_cascade(label="Financeiro", menu=self.filemenu4)

        # APLICA O MENU
        self.root.config(menu=self.barrademenu)

        self.imgLogo9=PhotoImage(file=pastaApp+"\\IMG\\new.png")
        self.l_logo=Label(self.root,image=self.imgLogo9)
        self.l_logo.place(x=-300,y=-250)      
        
        self.frame_botoes = Frame(self.root)
        self.frame_botoes.place(relx=0.0, rely=0.0, anchor="nw", width=810, height=82)

        self.frame_cliente = Frame(self.frame_botoes)
        self.imgLogo = PhotoImage(file=pastaApp + "\\IMG\\Manager1.png")
        self.btn_cliente = Button(self.frame_cliente,image=self.imgLogo,relief="ridge",borderwidth=0, activebackground="white", command=self.janela_cadastrocliente,width=69,height=57, cursor="hand2")
        self.frame_cliente.grid(row=0, column=1, padx=0, pady=1, sticky="nsew")
        self.btn_cliente.pack(expand=True, fill="both")
        self.lbl_cliente = Label(self.frame_cliente,text="CADASTRO [F1]",font=("arial", 8), foreground="white",background="black", width=16, anchor="center")
        self.lbl_cliente.pack(pady=2)

        self.frame_agenda = Frame(self.frame_botoes)
        self.imgLogo2 = PhotoImage(file=pastaApp + "\\IMG\\calendar.png")
        self.btn_agenda = Button(self.frame_agenda, image=self.imgLogo2, relief="ridge", borderwidth=0, activebackground="white", command=self.janela_agendaconsulta, width=69, height=57, cursor="hand2")
        self.btn_agenda.pack(expand=True, fill="both")
        self.lbl_agenda = Label(self.frame_agenda,text="AGENDA [F2]", font=("arial", 8),foreground="white",background="black",width=16,anchor="center")
        self.lbl_agenda.pack(pady=2)
        self.frame_agenda.grid(row=0, column=2, padx=0, pady=1, sticky="nsew")

        self.frame_estoque = Frame(self.frame_botoes)
        self.imgLogo3 = PhotoImage(file=pastaApp + "\\IMG\\Box1.png")
        self.btn_estoque = Button(self.frame_estoque,image=self.imgLogo3, relief="ridge",borderwidth=0, activebackground="white", command=self.janela_estoque, width=69, height=57, cursor="hand2")
        self.btn_estoque.pack(expand=True, fill="both")
        self.lbl_estoque = Label(self.frame_estoque,text="ESTOQUE [F3]", font=("arial", 8), foreground="white",background="black",width=16,anchor="center")
        self.lbl_estoque.pack(pady=2)
        self.frame_estoque.grid(row=0, column=3, padx=0, pady=1, sticky="nsew")

        self.frame_exames = Frame(self.frame_botoes) 
        self.imgLogo4 = PhotoImage(file=pastaApp + "\\IMG\\Test Passed1.png")
        self.btn_exames = Button(self.frame_exames,image=self.imgLogo4,relief="ridge",borderwidth=0, activebackground="white", command=self.janela_exames,width=69, height=57, cursor="hand2")
        self.btn_exames.pack(expand=True, fill="both")
        self.lbl_exames = Label(self.frame_exames,text="EXAMES [F4]", font=("arial", 8), foreground="white", background="black", width=16, anchor="center")
        self.lbl_exames.pack(pady=2)
        self.frame_exames.grid(row=0, column=4, padx=0, pady=1, sticky="nsew")

        self.frame_editar = Frame(self.frame_botoes)
        self.imgLogo6 = PhotoImage(file=pastaApp + "\\IMG\\Document1.png")
        self.btn_editar = Button(self.frame_editar,image=self.imgLogo6,relief="ridge", borderwidth=0, activebackground="white", command=self.janela_editar_cadastro, width=69,height=57, cursor="hand2")
        self.btn_editar.pack(expand=True, fill="both")
        self.lbl_editar = Label(self.frame_editar,text="EDITAR [F5]",font=("arial", 8), foreground="white",background="black",width=16,anchor="center")
        self.lbl_editar.pack(pady=2)
        self.frame_editar.grid(row=0, column=5, padx=0, pady=1, sticky="nsew")

        self.frame_financeiro = Frame(self.frame_botoes)
        self.imgLogo7 = PhotoImage(file=pastaApp + "\\IMG\\Money Bag1.png")
        self.btn_financeiro = Button(self.frame_financeiro,image=self.imgLogo7, relief="ridge", borderwidth=0, activebackground="white", command=self.janela_financeiro, width=69, height=57, cursor="hand2")
        self.btn_financeiro.pack(expand=True, fill="both")
        self.lbl_financeiro = Label(self.frame_financeiro, text="FINANCEIRO [F6]", font=("arial", 8), foreground="white", background="black", width=16, anchor="center")
        self.lbl_financeiro.pack(pady=2)
        self.frame_financeiro.grid(row=0, column=6, padx=0, pady=1, sticky="nsew")

        self.frame_resultados = Frame(self.frame_botoes)
        self.imgLogo20 = PhotoImage(file=pastaApp + "\\IMG\\Resultado.png")
        self.btn_resultado = Button(self.frame_resultados, image=self.imgLogo20, relief="ridge", borderwidth=0, activebackground="white", command=self.janela_resultados, width=69, height=57, cursor="hand2")
        self.btn_resultado.pack(expand=True, fill="both")
        self.lbl_resultado = Label(self.frame_resultados, text="RESULTADOS [F7]",font=("arial", 8), foreground="white", background="black", width=16, anchor="center")
        self.lbl_resultado.pack(pady=2)
        self.frame_resultados.grid(row=0, column=7, padx=0, pady=1, sticky="nsew")

        self.frame_sair = Frame(self.frame_botoes)
        self.imgLogo5 = PhotoImage(file=pastaApp + "\\IMG\\Cancel1.png")
        self.btn_sair = Button(self.frame_sair,image=self.imgLogo5,relief="ridge", borderwidth=0, activebackground="white", command=self.tecla_sair, width=69, height=57, cursor="hand2")
        self.btn_sair.pack(expand=True, fill="both")
        self.btn_sair.bind("<Button-1>", lambda event: self.cancelar_tela_principal())
        self.lbl_sair = Label(self.frame_sair,text="FECHAR [F8]",font=("arial", 8),foreground="white",background="black",width=16,anchor="center")
        self.lbl_sair.pack(pady=2)
        self.frame_sair.grid(row=0, column=8, padx=0, pady=1, sticky="nsew")

        self.frame1 = Frame(self.root, borderwidth=1, relief="raised", background="#DCDCDC")
        self.frame1.pack(side=BOTTOM, fill=X)

        self.imgLogo11 = PhotoImage(file=pastaApp + "\\IMG\\empresa.png")
        Label(self.frame1, image=self.imgLogo11, background="#DCDCDC").pack(side=LEFT, padx=5)
        Label(self.frame1, text="EMPRESA : LABORATÓRIO SÃO BENTO", foreground="black", font=('calibri', 10, 'bold'), background="#DCDCDC").pack(side=LEFT, padx=0)
        
        self.imgLogo10 = PhotoImage(file=pastaApp + "\\IMG\\iMac.png")
        #self.usuario=usuario
        Label(self.frame1, image=self.imgLogo10, background="#DCDCDC").pack(side=LEFT, padx=1)
        Label(self.frame1, text="USUÁRIO : Suporte", foreground="black", font=('calibri', 10, 'bold'), background="#DCDCDC").pack(side=LEFT, padx=0)
        #+self.usuario
        
        self.imgLogo12 = PhotoImage(file=pastaApp + "\\IMG\\bd.png")
        Label(self.frame1, text="", background="#DCDCDC", height=1).pack(side=LEFT, padx=5)
        Label(self.frame1, image=self.imgLogo12, background="#DCDCDC").pack(side=LEFT, padx=1)
        self.lbempresa2 = Label(self.frame1, foreground="black", font=('calibri', 10, 'bold'), background="#DCDCDC")
        self.lbempresa2.pack(side=LEFT, padx=0)
        self.verificar_status_servidor()

        self.lbsuporte=Label(self.frame1,text="Ajuda?(65)9 81217628",foreground="black",font=('calibri',10,'bold'),background="#DCDCDC")
        self.lbsuporte.place(x=650,y=10,width=150,height=18)

        self.imgLogo15=PhotoImage(file=pastaApp+"\\IMG\\Headset.png")
        self.l_logo=Label(self.frame1,image=self.imgLogo15,background="#DCDCDC")
        self.l_logo.place(x=630,y=5)

        self.lbemail=Label(self.frame1,text="suporte@syslab.com.br",foreground="black",font=('calibri',10,'bold'),background="#DCDCDC")
        self.lbemail.place(x=834,y=10,width=150,height=20)

        self.imgLogo16=PhotoImage(file=pastaApp+"\\IMG\\Mail.png")
        self.l_logo=Label(self.frame1,image=self.imgLogo16,background="#DCDCDC")
        self.l_logo.place(x=815,y=5)
        
        frame_direita = Frame(self.frame1, background="#DCDCDC")
        frame_direita.pack(side=RIGHT)

        self.imgLogo13 = PhotoImage(file=pastaApp + "\\IMG\\relogio.png")
        Label(frame_direita, image=self.imgLogo13, background="#DCDCDC").pack(side=LEFT, padx=0)
        self.label11 = Label(frame_direita, font=('calibri', 20, 'bold'), foreground="black", background="#DCDCDC")
        self.label11.pack(side=LEFT, padx=3)
        self.time()

        self.imgLogo14 = PhotoImage(file=pastaApp + "\\IMG\\calendario.png")
        Label(frame_direita, image=self.imgLogo14, background="#DCDCDC").pack(side=LEFT, padx=0)
        self.label12 = Label(frame_direita, fg="black", font=("calibri", 20, "bold"), background="#DCDCDC")
        self.label12.pack(side=LEFT, padx=3)
        self.dataatual()   
        
    
    #Metódos para abrir as janelas dos formulários usando o mouse.
    def janela_agendaconsulta(self):
        AgendaConsulta(self.root)
    def janela_cadastrocliente(self):
        CadastroDeClientes(self.root)
    def janela_exames(self):
        Exames(self.root)
    def janela_editar_cadastro(self):
        EditarCadastroDeClientes(self.root)
    def janela_estoque(self):
        JanelaEstoque(self.root)
    def janela_financeiro(self):
        Financeiro(self.root)
    def janela_resultados(self):
        TelaResultados(self.root)  

    #Metódos para abrir as janelas dos formulários usando as teclas de atalho no teclado.
    def tecla_cadastro(self, event):
        self.janela_cadastrocliente()
    def tecla_agenda(self, event):
        self.janela_agendaconsulta()
    def tecla_exames(self, event):
        self.janela_exames()
    def tecla_editarcadastro(self, event):
        self.janela_editar_cadastro()
    def tecla_estoque(self, event):
        self.janela_estoque()
    def tecla_financeiro(self, event):
        self.janela_financeiro()
    #def tecla_janela_resultados(self, event):
        #self.janela_resultados()
    def tecla_sair(self, event):
        self.cancelar_tela_principal()

    def cancelar_tela_principal(self):
        resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja sair?", cor_fundo="#A9A9A9", cor_texto="black")
        if resposta:
            self.root.quit()
      
    def verificar_status_servidor(self):
        status = self.banco.conectar()
        self.lbempresa2.config(text=f"SERVIDOR: {status}")
        if status == "Inativo":
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto="Erro ao conectar \nno banco de dados!", cor_fundo="#A9A9A9",cor_texto="black", caminho_img=pastaApp + "\\IMG\\erro.png")
        self.root.after(2000, self.verificar_status_servidor)  

    def dataatual(self):
        self.date = datetime.now()
        self.format_date = f"{self.date:%d/%m/%Y}"
        self.label12.config(text=self.format_date)

    def time(self):
        self.vtime = strftime('%H:%M:%S %p')
        self.label11.config(text=self.vtime)
        self.label11.after(1000, self.time)

    def nao_fechar(self):
        self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto=" Fechar sistema pressione [F8]!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
