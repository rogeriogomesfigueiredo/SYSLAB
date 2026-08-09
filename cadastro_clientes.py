import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from utils.formatacao import Formatacao
from config import pastaApp

class CadastroDeClientes:
    def __init__(self, root_pai):
        self.banco = BancoDeDados()
        self.centralizador = CentralizadorDeJanelas()
        self.mensagem = CaixaMensagemPersonalizada()
        self.formatacao = Formatacao()

        self.root_pai = root_pai
        self.toplevel = Toplevel(root_pai)
        self.centralizador.centralizar_toplevel(self.toplevel, 780, 500, root_pai)
        self.toplevel.configure(background="#e0e0e0")
        self.toplevel.overrideredirect(1)

        #Teclas de atalho usadas no teclado.
        self.toplevel.bind("<F1>", self.tecla_salvar)
        self.toplevel.bind("<F2>", self.tecla_sair)

        lb_clientes = Label(self.toplevel, text="CADASTRO DE CLIENTES",bg="#2F3542",fg="white",font=("Segoe UI", 16, "bold"))
        lb_clientes.place(x=0, y=0, width=780, height=70)

        frm1 = LabelFrame(self.toplevel, text="Dados do Paciente", relief="solid", borderwidth=1, background="#F5F6FA", font=("candara", 10, "italic"))
        frm1.place(x=5, y=75, width=770, height=340)

        frame_funcao = LabelFrame(self.toplevel, text="Configurações:", borderwidth=1, relief="solid",background="#e0e0e0", font=("candara", 10, "italic"))
        frame_funcao.place(x=5,y=430, width=770,height=62)

        frame_borda_estado = Frame(self.toplevel,bg="black")
        frame_borda_estado.place(x=17, y=309, width=332, height=32)  

        frame_borda_sexo = Frame(self.toplevel,bg="black")
        frame_borda_sexo.place(x=17, y=359, width=177, height=32)

        frame_borda_estado_civil = Frame(self.toplevel,bg="black")
        frame_borda_estado_civil.place(x=587, y=109, width=178, height=32)

        self.label_nome = Label(self.toplevel, text="NOME", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_nome.place(x=12, y=90, width=50, height=20)
        self.entry_nome = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_nome.place(x=17, y=110, width=375, height=30)

        self.label_telefone = Label(self.toplevel, text="TELEFONE", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_telefone.place(x=13, y=140, width=80, height=20)
        self.entry_telefone = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_telefone.bind("<KeyRelease>",lambda e: self.formatacao.formatar_telefone(self.entry_telefone, e))
        self.entry_telefone.place(x=17, y=160, width=220, height=30)

        self.label_email = Label(self.toplevel, text="E-MAIL", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_email.place(x=17, y=190, width=50, height=20)
        self.entry_email = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_email.place(x=17, y=210, width=360, height=30)

        self.label_cpf = Label(self.toplevel, text="CPF", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_cpf.place(x=13, y=240, width=40, height=20)
        self.entry_cpf = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_cpf.bind("<KeyRelease>",lambda e: self.formatacao.formatar_cpf(self.entry_cpf, e))
        self.entry_cpf.place(x=17, y=260, width=260, height=30)

        self.label_cidade = Label(self.toplevel, text="CIDADE", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_cidade.place(x=300, y=240, width=80, height=20)
        self.entry_cidade = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_cidade.place(x=310, y=260, width=450, height=30)

        self.label_estado = Label(self.toplevel, text="ESTADO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_estado.place(x=17, y=290, width=60, height=18)
        self.combobox3 = ttk.Combobox(self.toplevel,font=("calibri", 15),
            values=[
                "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo",
                "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais",
                "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
                "Santa Catarina", "São Paulo", "Sergipe", "Tocantins", "Distrito Federal"
            ])
        self.combobox3.place(x=18, y=310, width=330, height=30)

        self.label_bairro = Label(self.toplevel, text="BAIRRO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_bairro.place(x=365, y=290, width=60, height=20)
        self.entry_bairro = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_bairro.place(x=370, y=310, width=390, height=30)

        self.label_data_nascimento = Label(self.toplevel, text="DATA NASCIMENTO",background="#e0e0e0", foreground="black",font=("arial", 10, "bold"))
        self.label_data_nascimento.place(x=410, y=90, width=140, height=20)
        self.entry_data_nascimento = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_data_nascimento.bind("<KeyRelease>",lambda e: self.formatacao.formatar_data(self.entry_data_nascimento, e))
        self.entry_data_nascimento.place(x=415, y=110, width=150, height=30)

        self.label_endereco = Label(self.toplevel, text="ENDEREÇO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_endereco.place(x=220, y=140, width=140, height=20)
        self.entry_endereco = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_endereco.place(x=255, y=160, width=390, height=30)

        self.label_numero = Label(self.toplevel, text="Nº", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_numero.place(x=665, y=141, width=30, height=18)
        self.entry_numero = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_numero.place(x=670, y=160, width=90, height=30)

        self.label_estado_civil = Label(self.toplevel, text="ESTADO CIVIL",background="#e0e0e0", foreground="black",font=("arial", 10, "bold"))
        self.label_estado_civil.place(x=580, y=88, width=110, height=18)
        self.combobox1 = ttk.Combobox(self.toplevel, font=("calibri", 15),values=["Solteiro", "Casado", "Viúvo", "Divorciado"])
        self.combobox1.place(x=588, y=110, width=175, height=30)

        self.label_profissao = Label(self.toplevel, text="PROFISSÃO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_profissao.place(x=384, y=190, width=90, height=20)
        self.entry_profissao = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_profissao.place(x=390, y=210, width=370, height=30)

        self.label_sexo = Label(self.toplevel, text="SEXO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_sexo.place(x=10, y=341, width=50, height=18)
        self.combobox2 = ttk.Combobox(self.toplevel, font=("calibri", 15),values=["Masculino", "Feminino", "Outros"])
        self.combobox2.place(x=18, y=360, width=175, height=30)

        self.label_complemento = Label(self.toplevel, text="COMPLEMENTO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_complemento.place(x=205, y=341, width=111, height=18)
        self.entry_complemento = Entry(self.toplevel, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_complemento.place(x=210, y=360, width=550, height=30)

        btn_close = Button(self.toplevel, text="X", bg="red", fg="white", cursor="hand2", command=self.toplevel.destroy, bd=0)
        btn_close.place(x=750, y=5, width=25, height=20)

        self.botao_cancelar = Button(self.toplevel, borderwidth=1, text="     FECHAR [F2]",relief="solid", background="#E8F0F1",foreground="black", cursor="hand2",font=("arial", 10, "bold"),command=self.cancelar)
        self.botao_cancelar.place(x=405, y=450, width=120, height=32)
        self.imgLogo2 = PhotoImage(file=pastaApp + "\\IMG\\x.png")
        self.l_logo1 = Label(self.toplevel, image=self.imgLogo2, background="#E8F0F1")
        self.l_logo1.place(x=407, y=453)

        self.botao_salvar = Button(self.toplevel, borderwidth=1, text="     SALVAR [F1]",relief="solid", background="#E8F0F1",foreground="black", cursor="hand2",font=("arial", 10, "bold"),command=self.salvar)
        self.botao_salvar.place(x=280, y=450, width=120, height=32)
        self.imgLogo1 = PhotoImage(file=pastaApp + "\\IMG\\save.png")
        self.l_logo = Label(self.toplevel, image=self.imgLogo1, background="#E8F0F1")
        self.l_logo.place(x=283, y=452)

        self.toplevel.bind("<Button-1>", self.start_move)
        self.toplevel.bind("<B1-Motion>", self.do_move)


    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = event.x_root - self.x
        y = event.y_root - self.y
        self.toplevel.geometry(f"+{x}+{y}")

    def entry_on(self, event):
        if  self.entry_nome.get() == "Nome....":
                self.entry_nome.delete(0, "end")
                self.entry_nome.config(fg="black")

    def tecla_salvar(self, event):
        self.salvar()

    def tecla_sair(self, event):
        self.cancelar()

    def cancelar_formulario(self):
        self.toplevel.destroy()

    def cancelar(self):
        resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja sair?",cor_fundo="#A9A9A9",cor_texto="black")
        if resposta:
            self.toplevel.destroy()
        else:
            self.entry_nome.focus()
    
    def salvar(self):
        self.banco.conectar()
        nome = self.entry_nome.get().strip()
        telefone = self.entry_telefone.get().strip()
        cpf = self.entry_cpf.get().strip()
        cidade = self.entry_cidade.get().strip()
        email = self.entry_email.get().strip()
        estado = self.combobox3.get().strip()
        bairro = self.entry_bairro.get().strip()
        datanascimento = self.entry_data_nascimento.get().strip()
        endereco = self.entry_endereco.get().strip()
        numero = self.entry_numero.get().strip()
        estadocivil = self.combobox1.get().strip()
        profissao = self.entry_profissao.get().strip()
        sexo = self.combobox2.get().strip()
        complemento = self.entry_complemento.get().strip()
        if (nome == "" or telefone == "" or cpf == "" or cidade == "" or email == "" or estado == "" or bairro == "" or datanascimento == "" or endereco == "" or numero == "" or estadocivil == "" or profissao == "" or sexo == "" or complemento == ""):
            self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto=" Preencha todos os campos!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja sair?",cor_fundo="#A9A9A9",cor_texto="black")
            if resposta:
                codigo_sql = "INSERT INTO sys_lab_clientes (nome, telefone, email, cpf, cidade, estado, bairro, datanascimento,endereco,numero, estadocivil, profissao, sexo, complemento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                valores_sql = (nome, telefone, email, cpf, cidade, estado, bairro, datanascimento, endereco, numero, estadocivil, profissao,sexo, complemento)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Sucesso",texto="Sucesso ao Salvar",cor_fundo="#A9A9A9",cor_texto="black",caminho_img=pastaApp + "\\IMG\\sucesso.png")
                self.formatacao.limpar_todos_campos(self.toplevel)
                self.entry_nome.focus()
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro",texto=f"Erro ao inserir....{e}",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")
        finally:
            if self.banco.conexao:
                self.banco.conexao.close()
