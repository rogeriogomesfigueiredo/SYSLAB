from tkinter import *
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from config import pastaApp
from telas.tela_principal import TelaPrincipal

class TelaLogin:
    def __init__(self, root):
        self.banco = BancoDeDados()
        self.centralizador = CentralizadorDeJanelas()
        self.mensagem = CaixaMensagemPersonalizada()
        
        self.root = root
        self.root.configure(background="#DCDCDC")
        self.root.overrideredirect(1)
        self.centralizador.centralizar_janela(self.root, 850, 400)

        #Teclas de atalho usadas no teclado.
        self.root.bind("<F10>", self.tecla_entrar)
        self.root.bind("<F11>", self.tecla_sair)

        self.variavel_senha = StringVar()

        self.logo_sistema = PhotoImage(file=pastaApp + "\\IMG\\logosyslab.png")
        Label(self.root, image=self.logo_sistema, bg="#DCDCDC").place(x=-30, y=-1)

        self.img_person = PhotoImage(file=pastaApp + "\\IMG\\img.png")
        Label(self.root, image=self.img_person, bg="#DCDCDC").place(x=250, y=200)

        self.frame_login = Frame(self.root, bg="#DCDCDC")
        self.frame_login.place(x=500, y=150, width=330, height=200)
       
        Label(self.frame_login, text="LOGIN", bg="#DCDCDC", font="arial 8 bold").place(x=69, y=90)
        self.icon_user = PhotoImage(file=pastaApp + "\\IMG\\fuser.png")
        Label(self.frame_login, image=self.icon_user, bg="#DCDCDC").place(x=120, y=85)

        Label(self.frame_login, text="SENHA", bg="#DCDCDC", font="arial 8 bold").place(x=69, y=130)
        self.icon_pass = PhotoImage(file=pastaApp + "\\IMG\\fsenha.png")
        Label(self.frame_login, image=self.icon_pass, bg="#DCDCDC").place(x=120, y=125)
     
        self.entry_usuario = Entry(self.frame_login, bg="white", relief="ridge", borderwidth=1)
        self.entry_usuario.place(x=160, y=90, width=150, height=20)
        self.entry_usuario.focus()

        self.entry_senha = Entry(self.frame_login, bg="white", relief="ridge",borderwidth=1, textvariable=self.variavel_senha, show="*")
        self.entry_senha.place(x=160, y=130, width=150, height=20)

        self.btn_entrar = Button(self.root, text="ENTRAR [F10]", bg="green", fg="white",borderwidth=3, font="arial 9", relief="ridge",command=self.logado)
        self.btn_entrar.place(x=620, y=330, width=90, height=30)

        self.btn_sair = Button(self.root, text="FECHAR [F11]", bg="red", fg="white",borderwidth=3, font="arial 9", relief="ridge",command=self.sair)
        self.btn_sair.place(x=720, y=330, width=90, height=30)
        
        self.frame_footer = Frame(self.root, bg="#2F4F4F")
        self.frame_footer.place(x=0, y=380, width=860, height=25)

        Label(self.frame_footer, text="Sistema de Gestão Versão 1.0   |",bg="#2F4F4F", fg="white", font=("Arial", 9, "bold"), anchor="w").pack(side="left", padx=5)

        self.label_status = Label(self.frame_footer, text="Banco: ...",bg="#2F4F4F", fg="white", font=("Arial", 9, "bold"))
        self.label_status.pack(side="left", padx=5)

        Label(self.frame_footer, text=f"IP do Servidor: {self.banco.ip}",bg="#2F4F4F", fg="white", font=("Arial", 9, "bold")).pack(side="left", padx=5)
        self.atualizar_status_banco()
    
    def atualizar_status_banco(self):
        status = self.banco.conectar()
        if status == 'Ativo':
            self.label_status.config(text="Status do Servidor: Ativo |", fg="white")
        else:
            self.label_status.config(text="Status do Servidor: Inativo |", fg="#FF4040")
            self.mensagem.alerta_erro_sucesso(parent=self.root,titulo="Erro",texto="Não foi possível conectar ao banco.",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")
            self.root.after(1000, self.atualizar_status_banco)

    def logado(self):
        status = self.banco.conectar()
        if status != "Ativo":
            self.mensagem.alerta_erro_sucesso(titulo="Erro",texto="Não foi possível conectar ao banco.",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")
            return
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        if usuario == "" or senha == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto="Preencha todos os campos!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
            return
        try:
            codigo_sql = "SELECT * FROM sys_lab_acesso WHERE usuario=%s AND senha=%s"
            valores_sql = (usuario,senha) 
            self.banco.cursor.execute(codigo_sql, valores_sql)
            resultado_sql = self.banco.cursor.fetchone()
            if  resultado_sql:
                self.root.withdraw()
                TelaPrincipal(self.root, usuario)
            else:
                self.entry_usuario.delete(0, END)
                self.entry_senha.delete(0, END)
                self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto="Usuário ou senha incorretos!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
                self.entry_usuario.focus()

        except Exception as e:
            print("Erro em logado():", e)
            self.mensagem.alerta_erro_sucesso(titulo="Erro",texto="Erro ao verificar login!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")

    def sair(self):
        resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja sair?",cor_fundo="#A9A9A9",cor_texto="black")
        if resposta:
            self.root.destroy()

    def tecla_entrar(self, event):self.logado()

    def tecla_sair(self, event):self.sair()
