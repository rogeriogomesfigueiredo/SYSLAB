from tkinter import *
from tkinter import ttk
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from utils.formatacao import Formatacao
from config import pastaApp

class AgendaConsulta:
    def __init__(self, root_pai):
        self.banco = BancoDeDados()
        self.centralizador = CentralizadorDeJanelas()
        self.mensagem = CaixaMensagemPersonalizada()
        self.formatacao = Formatacao()

        self.root_pai = root_pai
        self.toplevel = Toplevel(root_pai)
        self.toplevel.overrideredirect(True)
        self.toplevel.configure(background="#e0e0e0")
        self.centralizador.centralizar_toplevel(self.toplevel, 850, 360, root_pai)

        #Teclas de atalho usadas no teclado.
        self.toplevel.bind("<F1>", self.tecla_salvar)
        self.toplevel.bind("<F2>", self.tecla_sair)
        
        self.label_clientes = Label(self.toplevel,text="         AGENDAMENTO DE EXAMES",background="#2F3542",foreground="white",font=("calibri", 20, "bold"))
        self.label_clientes.place(x=0, y=0, width=850, height=60)
     
        self.frame_2 = LabelFrame(self.toplevel,text="Dados do Paciente",background="#e0e0e0",borderwidth=1,relief="solid",font=("candara", 10, "italic"))
        self.frame_2.place(x=5, y=60, width=840, height=180)

        frame_borda_exame = Frame(self.toplevel,bg="black")
        frame_borda_exame.place(x=419, y=109, width=247, height=32)  

        frame_borda_especialista = Frame(self.toplevel,bg="black")
        frame_borda_especialista.place(x=16, y=159, width=192, height=32)

        self.botao_cancelar = Button(self.toplevel, borderwidth=1,text="      FECHAR [F2]",relief="solid",background="#E8F0F1",foreground="black", cursor="hand2",font=("arial", 10, "bold"),command=self.cancelar_cadastro)
        self.botao_cancelar.place(x=445, y=305, width=120, height=32)
        self.imagem_logo_2 = PhotoImage(file=pastaApp + "\\IMG\\x.png")
        self.label_logo_1 = Label(self.toplevel, image=self.imagem_logo_2, background="#E8F0F1")
        self.label_logo_1.place(x=447, y=308)

        self.botao_salvar = Button(self.toplevel, borderwidth=1,text="      SALVAR [F1]",relief="solid",background="#E8F0F1",foreground="black", cursor="hand2",font=("arial", 10, "bold"),command=self.salvar_cadastro)
        self.botao_salvar.place(x=312, y=305, width=120, height=32)
        self.imagem_logo_1 = PhotoImage(file=pastaApp + "\\IMG\\save.png")
        self.label_logo = Label(self.toplevel, image=self.imagem_logo_1, background="#E8F0F1")
        self.label_logo.place(x=314, y=307)

        self.label_nome_paciente = Label(self.toplevel,text="NOME",foreground="black",background="#e0e0e0",font=("arial", 10, "bold"))
        self.label_nome_paciente.place(x=7, y=90, width=60, height=20)
        self.entry_nome_paciente = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_nome_paciente.place(x=17, y=110, width=375, height=30)
        self.entry_nome_paciente.focus()

        self.label_exame = Label(self.toplevel, text="EXAME", background="#e0e0e0", foreground="black", font=("arial", 10, "bold"))
        self.label_exame.place(x=415, y=90, width=60, height=18)
        self.combobox_1 = ttk.Combobox(self.toplevel,font=("calibri", 15),values=["Covid-19", "Hemograma", "Urina", "Sangue"])
        self.combobox_1.place(x=420, y=110, width=245, height=30)
        self.combobox_1.set("")

        self.label_cpf = Label(self.toplevel, text="CPF", background="#e0e0e0", foreground="black", font=("arial", 10, "bold"))
        self.label_cpf.place(x=222, y=140, width=40, height=20)
        self.entry_cpf = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_cpf.bind("<KeyRelease>", lambda e: self.formatacao.formatar_cpf(self.entry_cpf, e))
        self.entry_cpf.place(x=225, y=160, width=200, height=30)

        self.label_contato = Label(self.toplevel, text="CONTATO", background="#e0e0e0", foreground="black", font=("arial", 10, "bold"))
        self.label_contato.place(x=625, y=141, width=80, height=18)
        self.entry_contato = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_contato.bind("<KeyRelease>", lambda e: self.formatacao.formatar_telefone(self.entry_contato, e))
        self.entry_contato.place(x=631, y=160, width=200, height=30)

        self.label_data = Label(self.toplevel, text="DATA", foreground="black", background="#e0e0e0", font=("arial", 10, "bold"))
        self.label_data.place(x=450, y=141, width=60, height=18)
        self.entry_data = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_data.bind("<KeyRelease>", lambda e: self.formatacao.formatar_data(self.entry_data, e))
        self.entry_data.place(x=460, y=160, width=150, height=30)

        self.label_horario = Label(self.toplevel, text="HORARIO", foreground="black", background="#e0e0e0", font=("arial", 10, "bold"))
        self.label_horario.place(x=680, y=90, width=85, height=20)
        self.entry_horario = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_horario.bind("<KeyRelease>", lambda e: self.formatacao.formatar_horario(self.entry_horario, e))
        self.entry_horario.place(x=690, y=110, width=140, height=30)

        self.label_especialista = Label(self.toplevel, text="ESPECIALISTA", foreground="black", background="#e0e0e0", font=("arial", 10, "bold"))
        self.label_especialista.place(x=15, y=140, width=100, height=18)
        self.combobox_2 = ttk.Combobox(self.toplevel,font=("calibri", 15),values=["Dr.Miguel", "Dr.André", "Dra.Rafaela", "Dra.Carol"])
        self.combobox_2.place(x=17, y=160, width=190, height=30)
        self.combobox_2.set("")

        btn_close = Button(self.toplevel, text="X", bg="red", fg="white", cursor="hand2",command=self.toplevel.destroy, bd=0)
        btn_close.place(x=820, y=5, width=25, height=20)

        self.toplevel.bind("<Button-1>", self.start_move)
        self.toplevel.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = event.x_root - self.x
        y = event.y_root - self.y
        self.toplevel.geometry(f"+{x}+{y}")

    def tecla_salvar(self, event):
        self.salvar_cadastro()

    def tecla_sair(self, event):
        self.cancelar_cadastro()

    def salvar_cadastro(self):
        self.banco.conectar()
        nome = self.entry_nome_paciente.get().strip()
        exame = self.combobox_1.get().strip()
        contato = self.entry_contato.get().strip()
        data = self.entry_data.get().strip()
        horario = self.entry_horario.get().strip()
        cpf = self.entry_cpf.get().strip()
        especialista = self.combobox_2.get().strip()
        if nome == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto="Digite todos os campos!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
            self.formatacao.limpar_todos_campos(self.toplevel)
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja salvar?",cor_fundo="#A9A9A9",cor_texto="black")
            if resposta:
                codigo_sql = "INSERT INTO sys_lab_exames (nome, exame, contato, data, horario, especialista, cpf) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores_sql = (nome, exame, contato, data, horario, especialista, cpf)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem",texto="Dados inseridos no banco de dados!",cor_fundo="#A9A9A9",cor_texto="black",caminho_img=pastaApp + "\\IMG\\sucesso.png")
                self.formatacao.limpar_todos_campos(self.toplevel)
                self.entry_nome_paciente.focus()
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro",texto=f"Erro ao inserir....{e}",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")
        finally:
            if self.banco.conexao:
                self.banco.conexao.close()

    def cancelar_cadastro(self):
        resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja sair?",cor_fundo="#A9A9A9",cor_texto="black")
        if  resposta:
                self.toplevel.destroy()
        else:
                self.entry_nome_paciente.focus()

