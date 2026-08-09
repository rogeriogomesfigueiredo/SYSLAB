from tkinter import *
from tkinter import ttk
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from utils.formatacao import Formatacao
from config import pastaApp

class JanelaEstoque:
    def __init__(self,root_pai):
        self.banco=BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()
        self.root_pai = root_pai
        self.toplevel = Toplevel(root_pai)
        self.toplevel.overrideredirect(True)
        self.toplevel.configure(background="#e0e0e0")
        self.centralizador.centralizar_toplevel(self.toplevel, 700, 400, root_pai)

        self.label_1=Label(self.toplevel,text="ESTOQUE DE PRODUTOS", background="#2F3542", foreground="white", font=("arial",20,"bold"))
        self.label_1.place(x=0,y=0,width=700,height=100)

        self.botao_cadastro_estoque=Button(self.toplevel,relief="flat",borderwidth=2,font=("arial 10 bold"),text="                 CADASTRO DE PRODUTO [F1]",background="#9a9898",foreground="white",anchor="center",activebackground="#9a9898", cursor="hand2",command=self.abrir_nova_janela)
        self.botao_cadastro_estoque.place(x=80,y=160,width=267,height=100)
        self.imagem_logo_1=PhotoImage(file=pastaApp+"\\IMG\\editarestoque.png")
        self.label_logo=Label(self.toplevel,image=self.imagem_logo_1,background="#9a9898")
        self.label_logo.place(x=85,y=180)
        self.toplevel.bind("<F1>", lambda event: self.abrir_nova_janela())   
        
        self.botao_pesquisar_estoque=Button(self.toplevel,relief="flat",borderwidth=2,font=("arial 10 bold"),text="                  PESQUISA DE PRODUTO [F2]",background="#9a9898",foreground="white",anchor="center",activebackground="#9a9898", cursor="hand2",command=self.abrir_nova_janela2)
        self.botao_pesquisar_estoque.place(x=375,y=160,width=265,height=100)
        self.imagem_logo_2=PhotoImage(file=pastaApp+"\\IMG\\pesquisarestoque.png")
        self.label_logo=Label(self.toplevel,image=self.imagem_logo_2,background="#9a9898")
        self.label_logo.place(x=382,y=180)
        self.toplevel.bind("<F2>", lambda event: self.abrir_nova_janela2()) 

        btn_close = Button(self.toplevel, text="X", bg="red", fg="white", cursor="hand2",command=self.toplevel.destroy, bd=0)
        btn_close.place(x=670, y=5, width=25, height=20)

        self.toplevel.bind("<Button-1>", self.start_move)
        self.toplevel.bind("<B1-Motion>", self.do_move)


    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = event.x_root - self.x
        y = event.y_root - self.y
        self.toplevel.geometry(f"+{x}+{y}")

    def cancelar_janela_estoque(self):
        self.toplevel.destroy()
        
    def tecla_cadastrar_produto(self, event):
        self.abrir_nova_janela()

    def tecla_pesquisar_produto(self, event):
        self.abrir_nova_janela2()

    def abrir_nova_janela(self):
        JanelaAdicionarEstoque(self.toplevel)

    def abrir_nova_janela2(self):
        JanelaPesquisarEstoque(self.toplevel)

class JanelaAdicionarEstoque:
    def __init__(self,root_pai):
        self.banco=BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()
        self.formatacao=Formatacao()
        
        self.janela_adicionar_estoque = Toplevel(root_pai)
        self.janela_adicionar_estoque.overrideredirect(True)
        self.janela_adicionar_estoque.configure(background="#939393")
        self.centralizador.centralizar_toplevel(self.janela_adicionar_estoque, 590, 340, root_pai)
        
        self.frame_1=Frame(self.janela_adicionar_estoque,background="#e0e0e0")
        self.frame_1.place(x=10,y=90,width=570,height=135)

        self.frame_2 = Frame(self.janela_adicionar_estoque,background="#e0e0e0")
        self.frame_2.place(x=10,y=280,width=570,height=45)  

        self.label_clientes=Label(self.janela_adicionar_estoque,text="CADASTRO DE PRODUTOS",background="#30497D",foreground="white",font=("calibri",20,"bold"))
        self.label_clientes.place(x=0,y=0,width=590,height=58)

        Label(self.janela_adicionar_estoque, text="Informações do produto", bg="#939393", fg="black",font=("Segoe UI Semibold", 14)).place(x=30, y=58)
        self.imagem_logo_exam = PhotoImage(file=pastaApp + "\\IMG\\img_produto.png")
        Label(self.janela_adicionar_estoque, image=self.imagem_logo_exam,background="#939393").place(x=6, y=58)
        

        Label(self.janela_adicionar_estoque, text="Ações", bg="#939393", fg="black",font=("Segoe UI Semibold", 14)).place(x=30, y=246)
        self.imagem_logo_acao = PhotoImage(file=pastaApp + "\\IMG\\img_configuracao.png")
        Label(self.janela_adicionar_estoque, image=self.imagem_logo_acao,background="#939393").place(x=6, y=246)

        self.botao_cancelar=Button(self.janela_adicionar_estoque, borderwidth=1,text="      FECHAR [F2]",relief="solid",background="#E8F0F1",foreground="black",font=("arial",10,"bold"),activebackground="#9a9898",activeforeground="white", cursor="hand2",command=self.cancelar_produto)
        self.botao_cancelar.place(x=300,y=287,width=120,height=32)
        self.imagem_logo_2=PhotoImage(file=pastaApp+"\\IMG\\x.png")
        self.label_logo_1=Label(self.janela_adicionar_estoque,image=self.imagem_logo_2,background="#E8F0F1")
        self.label_logo_1.place(x=302,y=290)
                
        self.botao_salvar=Button(self.janela_adicionar_estoque, borderwidth=1,text="     SALVAR [F1]",relief="solid",background="#E8F0F1",foreground="black",font=("arial",10,"bold"),activebackground="#9a9898",activeforeground="white", cursor="hand2",command=self.salvar_produto)
        self.botao_salvar.place(x=175,y=287,width=120,height=32)
        self.imagem_logo_1=PhotoImage(file=pastaApp+"\\IMG\\save.png")
        self.label_logo=Label(self.janela_adicionar_estoque,image=self.imagem_logo_1,background="#E8F0F1")
        self.label_logo.place(x=178,y=290)

        self.label_nome_produto=Label(self.janela_adicionar_estoque,text="NOME PRODUTO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_nome_produto.place(x=10,y=100,width=130,height=20)
        self.entry_nome_produto=Entry(self.janela_adicionar_estoque,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_nome_produto.place(x=17,y=120,width=355,height=30)
        self.entry_nome_produto.focus()

        self.label_quantidade=Label(self.janela_adicionar_estoque,text="QUANTIDADE",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_quantidade.place(x=400,y=100,width=100,height=20)
        self.entry_quantidade=Entry(self.janela_adicionar_estoque,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_quantidade.place(x=410,y=120,width=165,height=30)

        self.label_tipo=Label(self.janela_adicionar_estoque,text="TIPO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_tipo.place(x=600,y=100,width=100,height=18)
        self.combobox_1=ttk.Combobox(self.janela_adicionar_estoque,font=("calibri",15),values=["Unidade", "Pacote", "Kilograma", "Fardo","Caixa"])
        self.combobox_1.place(x=630,y=120,width=145,height=30)
        self.combobox_1.set("")

        self.label_data_validade=Label(self.janela_adicionar_estoque,text="DATA DE VALIDADE",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_data_validade.place(x=10,y=150,width=140,height=20)
        self.entry_data_validade=Entry(self.janela_adicionar_estoque,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_data_validade.bind("<KeyRelease>", lambda e: self.formatacao.formatar_data(self.entry_data_validade, e))
        self.entry_data_validade.place(x=17,y=170,width=160,height=30)

        self.label_observacao=Label(self.janela_adicionar_estoque,text="OBSERVAÇÂO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_observacao.place(x=170,y=150,width=150,height=20)
        self.entry_observacao=Entry(self.janela_adicionar_estoque,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_observacao.place(x=200,y=170,width=375,height=30)

        btn_close = Button(self.janela_adicionar_estoque, text="X", bg="red", fg="white", cursor="hand2",command=self.janela_adicionar_estoque.destroy, bd=0)
        btn_close.place(x=560, y=5, width=25, height=20)
        
        self.janela_adicionar_estoque.bind("<Button-1>", self.start_move_1)
        self.janela_adicionar_estoque.bind("<B1-Motion>", self.do_move_1)

    def start_move_1(self, event):
                self.x = event.x
                self.y = event.y
    
    def do_move_1(self, event):
                x = event.x_root - self.x
                y = event.y_root - self.y
                self.janela_adicionar_estoque.geometry(f"+{x}+{y}")


    def cancelar_janela_adicionar_estoque(self):
            self.janela_adicionar_estoque.destroy()

    def salvar_produto(self):
        self.banco.conectar()
        produto=self.entry_nome_produto.get().strip()
        quantidade=self.entry_quantidade.get().strip()
        tipo=self.combobox_1.get().strip()
        data_validade=self.entry_data_validade.get().strip()
        obs=self.entry_observacao.get().strip()
        if  produto=="":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Digite todos os campos!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return 
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Inserir o dado no sistema?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql= "INSERT INTO sys_lab_estoque (nome,quantidade,tipo,datavencimento,obs) VALUES(%s,%s,%s,%s,%s)"
                valores_sql=(produto, quantidade, tipo, data_validade, obs)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit() 
                self.mensagem.alerta_erro_sucesso(titulo="Sucesso", texto="Dados Salvos!", cor_fundo="#A9A9A9", caminho_img="IMG/sucesso.png")
                self.janela_adicionar_estoque.destroy()
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao inserir....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()
   
    def cancelar_produto(self):
        resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja sair?", cor_fundo="#A9A9A9", cor_texto="black")
        if  resposta:
            self.janela_adicionar_estoque.destroy()
        else:
            self.janela_adicionar_estoque.focus_force()


class JanelaPesquisarEstoque:
    def __init__(self, root_pai):
        self.toplevel = Toplevel(root_pai)
        self.banco = BancoDeDados()
        self.centralizador=CentralizadorDeJanelas()
        self.mensagem=CaixaMensagemPersonalizada()
        self.formatacao=Formatacao() 
        self.centralizador.centralizar_toplevel(self.toplevel, 1010, 500, root_pai)
        self.toplevel.overrideredirect(True)

        frame_tree = ttk.Frame(self.toplevel)
        frame_tree.place(x=7, y=98, width=995, height=397)

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading",font=("Segoe UI", 11, "bold"),background="#1E3D5F",foreground="white",borderwidth=0)
        self.style.configure("Treeview",font=("Segoe UI", 10),background="#C6E2FF",foreground="#000000",rowheight=32,fieldbackground="#B4CDCD")
        self.style.map("Treeview",background=[("selected", "#4a7efc")],foreground=[("selected", "#ffffff")])

        self.scrollbar = ttk.Scrollbar(frame_tree, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.tree_view = ttk.Treeview(frame_tree,columns=('codigo', 'nome', 'quantidade', 'tipo', 'data vencimento', 'obs'),show="headings",yscrollcommand=self.scrollbar.set)
        self.tree_view.column('codigo', minwidth=10, width=80)
        self.tree_view.column('nome', minwidth=60, width=160)
        self.tree_view.column('quantidade', minwidth=0, width=100)
        self.tree_view.column('tipo', minwidth=0, width=100)
        self.tree_view.column('data vencimento', minwidth=0, width=130)
        self.tree_view.column('obs', minwidth=0, width=200)
        self.tree_view.heading('codigo', text="CÓDIGO", anchor=W)
        self.tree_view.heading('nome', text="NOME", anchor=W)
        self.tree_view.heading('quantidade', text="QUANTIDADE", anchor=W)
        self.tree_view.heading('tipo', text="TIPO", anchor=W)
        self.tree_view.heading('data vencimento', text="DATA VENCIMENTO", anchor=W)
        self.tree_view.heading('obs', text="OBSERVAÇÃO", anchor=W)

        self.scrollbar.config(command=self.tree_view.yview)
        self.tree_view.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree_view.bind("<Double-1>", self.janela_pesquisa)

        try:
            self.banco.conectar()
            self.banco.cursor.execute("SELECT * FROM sys_lab_estoque ORDER BY id")
            resultado_sql = self.banco.cursor.fetchall()
            for i in resultado_sql:
                self.tree_view.insert("", "end", id=i[0], text=i[0], values=(i[0:]))
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao selecionar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()
        
        self.frame_1=Frame(self.toplevel,background="#1E3D5F")
        self.frame_1.place(x=-1,y=-1,width=1003,height=97)

        self.label_1=Label(self.toplevel,text="ESTOQUE DE PRODUTOS", background="#1E3D5F", font=("arial",15,"bold"),fg="white")
        self.label_1.place(x=5,y=25,width=280,height=30)

        self.entry_nome_cliente = Entry(self.toplevel, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_nome_cliente.place(x=7, y=67, width=582, height=30)
        self.entry_nome_cliente.insert(0, "Buscar....")
        self.entry_nome_cliente.config(fg="gray")

        self.botao_pesquisar_cliente = Button(self.toplevel, relief="flat", borderwidth=2, font=("arial 10 bold"), text="       PESQUISAR PRODUTO [F1]", background="#4a7efc", foreground="white", anchor="center", activebackground="#4a7efc",activeforeground="white" ,cursor="hand2",command=self.pesquisar)
        self.botao_pesquisar_cliente.place(x=590, y=67, width=204, height=30)
        self.imagem_logo_7=PhotoImage(file=pastaApp+"\\IMG\\icon3.png")
        self.label_logo_7=Label(self.toplevel,image=self.imagem_logo_7,background="#4a7efc")
        self.label_logo_7.place(x=591,y=67)

        self.entry_nome_cliente.bind("<FocusIn>", self.entry_on)
        self.entry_nome_cliente.bind("<FocusOut>", self.entry_of)

    def cancelar_janela_pesquisar_estoque(self):
        self.toplevel.destroy()

    def entry_on(self, event):
        if  self.entry_nome_cliente.get() == "Buscar....":
                self.entry_nome_cliente.delete(0, "end")
                self.entry_nome_cliente.config(fg="black")

    def entry_of(self, event):
        if  self.entry_nome_cliente.get() == "":
                self.entry_nome_cliente.insert(0, "Buscar....")
                self.entry_nome_cliente.config(fg="gray")

    def janela_pesquisa(self, event):
        item = self.tree_view.focus()
        if not item:
            return

        valores = self.tree_view.item(item, "values")

        self.janela_edicao = Toplevel(self.toplevel)
        self.janela_edicao.configure(background="#e0e0e0")
        self.janela_edicao.resizable(False, False)
        self.janela_edicao.title("Editar produto")
        self.janela_edicao.iconbitmap('IMG\\iconeprograma.ico')
        self.janela_edicao.resizable(False, False)
        central = CentralizadorDeJanelas()
        central.centralizar_toplevel(self.janela_edicao, 600, 280, self.toplevel)
    
        frame_editar_produto = LabelFrame(self.janela_edicao, text="Editar produto:", background="#e0e0e0",borderwidth=1, relief="solid", font=("candara", 10, "italic"))
        frame_editar_produto.place(x=10, y=10, width=580, height=180)

        frame_configuracao = LabelFrame(self.janela_edicao, text="Configuração:", background="#e0e0e0",borderwidth=1, relief="solid", font=("candara", 10, "italic"))
        frame_configuracao.place(x=10, y=200, width=580, height=70) 

        frame_borda_tipo = Frame(self.janela_edicao,bg="black")
        frame_borda_tipo.place(x=419,y=59,width=154,height=32)  

        self.label_codigo=Label(self.janela_edicao,text="CODIGO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_codigo.place(x=469,y=91,width=60,height=18)
        self.entry_codigo=Entry(self.janela_edicao,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_codigo.place(x=470,y=110,width=100,height=30)
        self.entry_codigo.insert(0, valores[0])

        self.label_nome_produto=Label(self.janela_edicao,text="NOME PRODUTO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_nome_produto.place(x=16,y=40,width=110,height=20)
        self.entry_nome_produto=Entry(self.janela_edicao,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_nome_produto.place(x=17,y=60,width=200,height=30)
        self.entry_nome_produto.insert(0, valores[1])

        self.label_quantidade=Label(self.janela_edicao,text="QUANTIDADE",background="#e0e0e0",foreground="black",font=("arial",10,"bold"))
        self.label_quantidade.place(x=243,y=40,width=100,height=20)
        self.entry_quantidade=Entry(self.janela_edicao,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_quantidade.place(x=250,y=60,width=150,height=30)
        self.entry_quantidade.insert(0, valores[2])

        self.label_tipo=Label(self.janela_edicao,text="TIPO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_tipo.place(x=386,y=40,width=100,height=18)
        self.combobox_1=ttk.Combobox(self.janela_edicao,font=("calibri",15),values=["Unidade", "Pacote", "Kilograma", "Fardo","Caixa"])
        self.combobox_1.place(x=420,y=60,width=152,height=30)
        self.combobox_1.set("")
        self.combobox_1.insert(0, valores[3])

        self.label_data_validade=Label(self.janela_edicao,text="DATA DE VALIDADE",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_data_validade.place(x=17,y=90,width=125,height=20)
        self.entry_data_validade=Entry(self.janela_edicao,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_data_validade.bind("<KeyRelease>", lambda e: self.formatacao.formatar_data(self.entry_data_validade, e))
        self.entry_data_validade.place(x=17,y=110,width=130,height=30)
        self.entry_data_validade.insert(0, valores[4])

        self.label_observacao=Label(self.janela_edicao,text="OBSERVAÇÂO",foreground="black",background="#e0e0e0",font=("arial",10,"bold"))
        self.label_observacao.place(x=142,y=90,width=150,height=20)
        self.entry_observacao=Entry(self.janela_edicao,borderwidth=1,relief="solid",font=("calibri",15))
        self.entry_observacao.place(x=170,y=110,width=280,height=30)
        self.entry_observacao.insert(0, valores[5])
  
        self.botao_atualizar = Button(frame_configuracao, borderwidth=1, relief="solid", text="       ATUALIZAR F[1]", font=("arial", 10, "bold"),bg="#E8F0F1", command=self.atualizarproduto)
        self.botao_atualizar.place(x=160, y=10, width=134, height=35)
        self.imgLogo3=PhotoImage(file=pastaApp+"\\IMG\\icon4.png")
        self.l_logo=Label(frame_configuracao,image=self.imgLogo3,background="#E8F0F1")
        self.l_logo.place(x=162,y=12)
        
        self.botao_excluir = Button(frame_configuracao, borderwidth=1 , text="      EXCLUIR F[2]", relief="solid" ,font=("arial", 10, "bold"),bg="#E8F0F1", command=self.excluirproduto)
        self.botao_excluir.place(x=310, y=10, width=133, height=35)
        self.imgLogo2=PhotoImage(file=pastaApp+"\\IMG\\icon2.png")
        self.l_logo=Label(frame_configuracao,image=self.imgLogo2,background="#E8F0F1")
        self.l_logo.place(x=312,y=12)   

    def cancelar_formulario(self):
        self.janela_edicao.destroy()

    def atualizarproduto(self):
        self.banco.conectar()
        nome = self.entry_nome_produto.get().strip()
        quantidade = self.entry_quantidade.get().strip()
        tipo = self.combobox_1.get().strip()
        data = self.entry_data_validade.get().strip()
        obs = self.entry_observacao.get().strip()
        id = self.entry_codigo.get().strip()
        if nome == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Selecione um produto para atualizar!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja atualizar o produto?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql = "UPDATE sys_lab_estoque SET nome=%s, quantidade=%s, tipo=%s, datavencimento=%s, obs=%s WHERE id=%s"
                valores_sql = (nome, quantidade, tipo, data, obs, id)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem", texto="Produto atualizado com sucesso!", cor_fundo="#A9A9A9", caminho_img="IMG/sucesso.png")
                self.tree_view.delete(*self.tree_view.get_children())     
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao atualizar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()

    def excluirproduto(self):
        self.banco.conectar()
        id = self.entry_codigo.get().strip()
        if id == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Selecione um produto para excluir!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação", texto="Deseja excluir?", cor_fundo="#A9A9A9", cor_texto="black")
            if resposta:
                codigo_sql = "DELETE FROM sys_lab_estoque WHERE id = %s"
                valores_sql=(id,)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem", texto="Produto excluído!", cor_fundo="#A9A9A9", caminho_img="IMG/sucesso.png")
                self.tree_view.delete(*self.tree_view.get_children())
                self.formatacao.limpar_todos_campos(self.toplevel)
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao excluir....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()

    def pesquisar(self):
        self.banco.conectar()
        consulta=self.entry_nome_cliente.get().strip()
        if  consulta == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Informe o nome para pesquisa!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            return 
        try:
            self.tree_view.delete(*self.tree_view.get_children())
            codigo_sql = 'SELECT * FROM sys_lab_estoque WHERE nome LIKE %s ORDER BY id'
            valores_sql=('%' + consulta + '%',)
            self.banco.cursor.execute(codigo_sql, valores_sql)
            resultado_sql = self.banco.cursor.fetchall()
            if len(resultado_sql) > 0:
                for i in resultado_sql:
                    self.tree_view.insert("", "end", id=i[0], text=i[0], values=(i[0:]))
            else:
                self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="A busca não obteve resultado!",cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
                self.entry_nome_cliente.delete(0,END)
        except  Exception as e:
                self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao editar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()