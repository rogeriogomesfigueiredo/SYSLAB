from tkinter import *
from tkinter import ttk
from tkinter import END
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from utils.formatacao import Formatacao
from config import pastaApp

class EditarCadastroDeClientes:
    def __init__(self,root_pai):
        self.banco=BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()
        self.formatacao=Formatacao()
        
        self.root_pai = root_pai
        self.toplevel = Toplevel(root_pai)
        self.toplevel.transient(root_pai)
        self.toplevel.title("")
        self.toplevel.iconbitmap('IMG\\iconeprograma.ico')
        self.toplevel.configure(background="#1E3D5F")
        self.toplevel.resizable(False, False)
        self.toplevel.grab_set()
        self.centralizador.centralizar_toplevel(self.toplevel, 1025, 509, root_pai)

        frame_tree = ttk.Frame(self.toplevel)
        frame_tree.place(x=10, y=99, width=1007, height=401)

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading",font=("Segoe UI", 11, "bold"),background="#1E3D5F",foreground="white",borderwidth=0)
        self.style.configure("Treeview",font=("Segoe UI", 10),background="#315B88",foreground="black",rowheight=30,fieldbackground="#5D7998")
        self.style.map("Treeview",background=[("selected", "#4a7efc")],foreground=[("selected", "black")])

        self.scrollbar = ttk.Scrollbar(frame_tree, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.tree_view=ttk.Treeview(frame_tree,columns=('id','nome', 'telefone', 'email', 'cpf', 'cidade', 'estado', 'bairro', 'datanascimento', 'endereco', 'numero', 'estadocivil', 'profissao', 'sexo', 'complemento'),show="headings", yscrollcommand=self.scrollbar.set)
        self.tree_view.column("id", width=0, stretch=False)
        self.tree_view.column('nome',minwidth=0,width=120)
        self.tree_view.column('telefone',minwidth=0,width=120)
        self.tree_view.column('email',minwidth=0,width=120)
        self.tree_view.column('cpf',minwidth=0,width=120)
        self.tree_view.column('cidade',minwidth=0,width=120)
        self.tree_view.column('estado',minwidth=0,width=120)
        self.tree_view.column('bairro',minwidth=0,width=120)
        self.tree_view.column('datanascimento',minwidth=0,width=150)
        self.tree_view.column('endereco',minwidth=0,width=120)
        self.tree_view.column('numero',minwidth=0,width=120)
        self.tree_view.column('estadocivil',minwidth=0,width=120)
        self.tree_view.column('profissao',minwidth=0,width=120)
        self.tree_view.column('sexo',minwidth=0,width=120)
        self.tree_view.column('complemento',minwidth=0,width=120)
        self.tree_view.heading("id", text="")
        self.tree_view.heading('nome',text="NOME",anchor=W)
        self.tree_view.heading('telefone',text="TELEFONE",anchor=W)
        self.tree_view.heading('email',text="EMAIL",anchor=W)
        self.tree_view.heading('cpf',text="CPF",anchor=W)
        self.tree_view.heading('cidade',text="CIDADE",anchor=W)
        self.tree_view.heading('estado',text="ESTADO",anchor=W)
        self.tree_view.heading('bairro',text="BAIRRO",anchor=W)
        self.tree_view.heading('datanascimento',text="DATA NASCIMENTO",anchor=W)
        self.tree_view.heading('endereco',text="ENDERECO",anchor=W)
        self.tree_view.heading('numero',text="NUMERO",anchor=W)
        self.tree_view.heading('estadocivil',text="ESTADOCIVIL",anchor=W)
        self.tree_view.heading('profissao',text="PROFISSAO",anchor=W)
        self.tree_view.heading('sexo',text="SEXO",anchor=W)
        self.tree_view.heading('complemento',text="COMPLEMENTO",anchor=W)
        self.scrollbar.config(command=self.tree_view.yview)
        self.tree_view.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree_view.tag_configure("par", background="#f2f2f2")
        self.tree_view.tag_configure("impar", background="#ffffff")

        self.tree_view.bind("<Double-1>", self.janela_pesquisa)

        self.banco.conectar()
        self.tree_view.delete(*self.tree_view.get_children())
        codigo_sql = 'SELECT * FROM sys_lab_clientes'
        self.banco.cursor.execute(codigo_sql)
        resultado_sql = self.banco.cursor.fetchall()
        
        for i, item in enumerate(resultado_sql):
            tag = "par" if i % 2 == 0 else "impar"
            self.tree_view.insert("","end",values=(item[0:]),tags=(tag,))

        self.frame_3 = Frame(self.toplevel,background="#1E3D5F")
        self.frame_3.place(x=0, y=0, width=1010, height=99)

        self.label_texto = Label(self.toplevel, text="EDITAR CADASTRO", foreground="white", background="#1E3D5F",font=("calibri", 20, "bold"))
        self.label_texto.place(x=10, y=20, width=230, height=20)

        #self.imagem_logo_10 = PhotoImage(file=pastaApp + "\\IMG\\Cancelar.png")
        #self.botao_fechar_formulario = Button(self.toplevel,image=self.imagem_logo_10,relief="flat",borderwidth=0,activebackground="#1E3D5F",background="#1E3D5F",cursor="hand2",command=self.cancelar)
        #self.botao_fechar_formulario.place(x=992, y=9, width=20, height=20)

        self.botao_consulta_paciente = Button(self.toplevel, relief="flat",borderwidth=2, activebackground="#2f66ff", activeforeground="white" ,font=("arial 9 bold"),text="        PESQUISAR PACIENTE [F1]",background="#2f66ff",foreground="white", cursor="hand2", command=self.pesquisar)
        self.botao_consulta_paciente.place(x=629, y=67, width=188, height=30)
        self.imagem_logo_5 = PhotoImage(file=pastaApp + "\\IMG\\icon3.png")
        Label(self.toplevel, image=self.imagem_logo_5,background="#2f66ff").place(x=630, y=68)

        self.entry_nome_cliente = Entry(self.toplevel, borderwidth=1,relief="solid", font=("calibri", 15))
        self.entry_nome_cliente.place(x=8, y=67, width=620, height=30)
        self.entry_nome_cliente.insert(0, "Buscar...")
        self.entry_nome_cliente.config(fg="gray")

        self.entry_nome_cliente.bind("<FocusIn>", self.entry_on)
        self.entry_nome_cliente.bind("<FocusOut>", self.entry_of)

    def cancelar(self):
        self.toplevel.destroy()

    def entry_on(self, event):
        if  self.entry_nome_cliente.get() == "Buscar...":
                self.entry_nome_cliente.delete(0, "end")
                self.entry_nome_cliente.config(fg="black")

    def entry_of(self, event):
        if  self.entry_nome_cliente.get() == "":
                self.entry_nome_cliente.insert(0, "Buscar...")
                self.entry_nome_cliente.config(fg="gray")      

    def janela_pesquisa(self, event):
        item = self.tree_view.focus()
        if not item:
            return
        valores = self.tree_view.item(item, "values")

        self.janela_edicao = Toplevel(self.toplevel)
        self.janela_edicao.transient(self.toplevel)
        self.janela_edicao.iconbitmap('IMG\\iconeprograma.ico')
        self.janela_edicao.configure(background="#e0e0e0")
        self.janela_edicao.resizable(False, False)
        self.janela_edicao.title("")
        central = CentralizadorDeJanelas()
        central.centralizar_toplevel(self.janela_edicao, 780, 470, self.toplevel)

        frame = LabelFrame(self.janela_edicao, borderwidth=1, relief="solid", text="Dados do Paciente", foreground="black",background="#e0e0e0", font=("candara", 10, "italic"))
        frame.place(x=5, y=20, width=770, height=440)

        frame_borda_estado = Frame(frame,bg="black")
        frame_borda_estado.place(x=17, y=249, width=332, height=32)  

        frame_borda_sexo = Frame(frame,bg="black")
        frame_borda_sexo.place(x=17, y=299, width=177, height=32)

        frame_borda_estado_civil = Frame(frame,bg="black")
        frame_borda_estado_civil.place(x=587, y=49, width=177, height=32)

        self.label_nome = Label(frame, text="NOME", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_nome.place(x=12, y=30, width=50, height=20)
        self.entry_nome = Entry(frame, relief="solid",font=("calibri", 15))
        self.entry_nome.place(x=17, y=50, width=375, height=30)
        self.entry_nome.insert(0, valores[1])

        self.label_telefone = Label(frame, text="TELEFONE", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_telefone.place(x=13, y=80, width=80, height=20)
        self.entry_telefone = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_telefone.bind("<KeyRelease>",lambda e: self.formatacao.formatar_telefone(self.entry_telefone, e))
        self.entry_telefone.place(x=17, y=100, width=220, height=30)
        self.entry_telefone.insert(0, valores[2])

        self.label_email = Label(frame, text="E-MAIL", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_email.place(x=17, y=130, width=50, height=20)
        self.entry_email = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_email.place(x=17, y=150, width=360, height=30)
        self.entry_email.insert(0, valores[3])

        self.label_cpf = Label(frame, text="CPF", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_cpf.place(x=13, y=180, width=40, height=20)
        self.entry_cpf = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_cpf.bind("<KeyRelease>",lambda e: self.formatacao.formatar_cpf(self.entry_cpf, e))
        self.entry_cpf.place(x=17, y=200, width=260, height=30)
        self.entry_cpf.insert(0, valores[4])

        self.label_cidade = Label(frame, text="CIDADE", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_cidade.place(x=300, y=180, width=80, height=20)
        self.entry_cidade = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_cidade.place(x=310, y=200, width=450, height=30)
        self.entry_cidade.insert(0, valores[5])
        
        self.label_estado = Label(frame, text="ESTADO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_estado.place(x=17, y=230, width=60, height=18)
        self.combobox3 = ttk.Combobox(frame,font=("calibri", 15),
            values=[
                "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo",
                "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais",
                "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
                "Santa Catarina", "São Paulo", "Sergipe", "Tocantins", "Distrito Federal"
            ])
        self.combobox3.place(x=18, y=250, width=330, height=30)
        self.combobox3.insert(0, valores[6])

        self.label_bairro = Label(frame, text="BAIRRO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_bairro.place(x=365, y=230, width=60, height=20)
        self.entry_bairro = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_bairro.place(x=370, y=250, width=390, height=30)
        self.entry_bairro.insert(0, valores[7])

        self.label_data_nascimento = Label(frame, text="DATA NASCIMENTO",background="#e0e0e0", foreground="black",font=("arial", 10, "bold"))
        self.label_data_nascimento.place(x=410, y=30, width=140, height=20)
        self.entry_data_nascimento = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_data_nascimento.bind("<KeyRelease>",lambda e: self.formatacao.formatar_data(self.entry_data_nascimento, e))
        self.entry_data_nascimento.place(x=415, y=50, width=150, height=30)
        self.entry_data_nascimento.insert(0, valores[8])

        self.label_endereco = Label(frame, text="ENDEREÇO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_endereco.place(x=220, y=80, width=140, height=20)
        self.entry_endereco = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_endereco.place(x=255, y=100, width=390, height=30)
        self.entry_endereco.insert(0, valores[9])

        self.label_numero = Label(frame, text="Nº", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_numero.place(x=665, y=82, width=30, height=17)
        self.entry_numero = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_numero.place(x=670, y=100, width=90, height=30)
        self.entry_numero.insert(0, valores[10])

        self.label_estado_civil = Label(frame, text="ESTADO CIVIL",background="#e0e0e0", foreground="black",font=("arial", 10, "bold"))
        self.label_estado_civil.place(x=580, y=30, width=110, height=18)
        self.combobox1 = ttk.Combobox(frame, font=("calibri", 15),values=["Solteiro", "Casado", "Viúvo", "Divorciado"])
        self.combobox1.place(x=588, y=50, width=175, height=30)
        self.combobox1.insert(0, valores[11])

        self.label_profissao = Label(frame, text="PROFISSÃO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_profissao.place(x=384, y=130, width=90, height=20)
        self.entry_profissao = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_profissao.place(x=390, y=150, width=370, height=30)
        self.entry_profissao.insert(0, valores[12])

        self.label_sexo = Label(frame, text="SEXO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_sexo.place(x=10, y=281, width=50, height=17)
        self.combobox2 = ttk.Combobox(frame, font=("calibri", 15),values=["Masculino", "Feminino", "Outros"])
        self.combobox2.place(x=18, y=300, width=175, height=30)
        self.combobox2.insert(0, valores[13])

        self.label_complemento = Label(frame, text="COMPLEMENTO", background="#e0e0e0",foreground="black", font=("arial", 10, "bold"))
        self.label_complemento.place(x=205, y=281, width=110, height=17)
        self.entry_complemento = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_complemento.place(x=210, y=300, width=550, height=30)
        self.entry_complemento.insert(0, valores[14])

        self.btnatualizar=Button(frame,relief="solid",borderwidth=1,font=("arial 9 bold"),text="        ATUALIZAR CLIENTE [F1]",background="#E8F0F1",foreground="black",anchor="center", cursor="hand2",activebackground="#9a9898",command=self.atualizar_paciente)
        self.btnatualizar.place(x=220,y=370,width=180,height=40)
        self.imgLogo3=PhotoImage(file=pastaApp+"\\IMG\\icon4.png")
        self.l_logo=Label(frame,image=self.imgLogo3,background="#E8F0F1")
        self.l_logo.place(x=222,y=374)

        self.btnexcluir=Button(frame,relief="solid",borderwidth=1,font=("arial 9 bold"),text="     EXCLUIR CLIENTE [F2]",background="#E8F0F1",foreground="black",anchor="center", cursor="hand2",activebackground="#9a9898",command=self.excluir_paciente)
        self.btnexcluir.place(x=410,y=370,width=180,height=40)
        self.imgLogo2=PhotoImage(file=pastaApp+"\\IMG\\icon2.png")
        self.l_logo=Label(frame,image=self.imgLogo2,background="#E8F0F1")
        self.l_logo.place(x=412,y=374)

    def cancelar_formulario(self):
        self.janela_edicao.destroy()
   
    def duploclick(self,event):
        self.tree_view.selection()
        for n in self.tree_view.selection():
            nome,cpf, = self.tree_view.item(n, 'values')
            self.entry_nome.insert(END,nome)
            self.entry_cpf.insert(END,cpf)
            
    def pesquisar(self):
        self.banco.conectar()
        consulta=self.entry_nome_cliente.get().strip()
        if  consulta=="":
                self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Informe o nome para pesquisa!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
                return 
        try:
            self.tree_view.delete(*self.tree_view.get_children())
            codigo_sql = 'SELECT * FROM sys_lab_clientes WHERE nome LIKE %s ORDER BY id'
            valores_sql=('%' + consulta + '%',)
            self.banco.cursor.execute(codigo_sql, valores_sql)
            resultado_sql = self.banco.cursor.fetchall()
            if len(resultado_sql) > 0:
                for i in resultado_sql:
                    self.tree_view.insert("", "end", id=i[0], text=i[0], values=(i[1:]))
            else:
                self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="A busca não obteve resultado!",cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
                self.entry_nome_cliente.delete(0,END)
        except  Exception as e:
                self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao editar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()

    def atualizar_paciente(self):
        self.banco.conectar()
        nome=self.entry_nome.get().strip()
        telefone=self.entry_telefone.get().strip()
        email=self.entry_email.get().strip()
        cpf=self.entry_cpf.get().strip()
        cidade=self.entry_cidade.get().strip()
        estado=self.combobox3.get().strip()
        bairro=self.entry_bairro.get().strip()
        nascimento=self.entry_data_nascimento.get().strip()
        endereco=self.entry_endereco.get().strip()
        numero=self.entry_numero.get().strip()
        estadocivil=self.combobox1.get().strip()
        profissao=self.entry_profissao.get().strip()
        sexo=self.combobox2.get().strip()
        complemento=self.entry_complemento.get().strip()
        if  nome == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="O formulario está com itens em branco!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja atualizaro cadastro?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql = 'UPDATE sys_lab_clientes SET nome = %s, telefone =%s, email =%s , cpf =%s , cidade =%s , estado =%s , bairro =%s , datanascimento =%s , endereco =%s , numero =%s , estadocivil =%s , profissao =%s , sexo =%s , complemento = %s WHERE cpf = %s'
                valores_sql=(nome, telefone, email, cpf, cidade, estado, bairro, nascimento, endereco, numero, estadocivil, profissao, sexo, complemento, cpf)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()  
                self.formatacao.limpar_todos_campos(self.toplevel)
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem", texto="Dados atualizados!", cor_fundo="#A9A9A9", cor_texto="black", caminho_img="IMG/alerta.png") 
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao atualizar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()

    def excluir_paciente(self):
        self.banco.conectar()
        nome=self.entry_nome.get().strip()
        cpf=self.entry_cpf.get().strip()
        if  nome =="":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Selecione um cliente para excluir!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return 
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja excluir o cliente?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql = 'DELETE FROM sys_lab_clientes WHERE cpf = %s'
                valores_sql=(cpf)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.formatacao.limpar_todos_campos(self.toplevel)
                self.mensagem.alerta_erro_sucesso(titulo="Sucesso", texto="Cliente excluido!", cor_fundo="#A9A9A9", caminho_img="IMG/sucesso.png")
                self.tree_view.delete(*self.tree_view.get_children())           
        except Exception  as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao deletar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()