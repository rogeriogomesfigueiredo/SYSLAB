from tkinter import *
from tkinter import ttk, filedialog
from datetime import datetime
from reportlab.pdfgen import canvas
from config import pastaApp
from utils.banco import BancoDeDados
from utils.centralizador import CentralizadorDeJanelas
from utils.mensagem import CaixaMensagemPersonalizada
from utils.formatacao import Formatacao

class Exames:
    def __init__(self, root_pai):
        self.banco = BancoDeDados()
        self.centralizador = CentralizadorDeJanelas()
        self.mensagem = CaixaMensagemPersonalizada()
        self.formatacao = Formatacao()
        self.root_pai = root_pai
        self.toplevel = Toplevel(root_pai)
        self.toplevel.overrideredirect(True)
        self.toplevel.configure(background="#2F3542")
        self.centralizador.centralizar_toplevel(self.toplevel, 1120, 507, root_pai)

        frame_header = Frame(self.toplevel,bg="#ffffff")
        frame_header.place(x=2, y=90, width=1115, height=40)

        frame_tree = ttk.Frame(self.toplevel)
        frame_tree.place(x=2, y=130, width=1115, height=377)

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading",font=("Segoe UI", 11, "bold"),background="#EFF5FD",foreground="black",borderwidth=0)
        self.style.configure("Treeview",font=("Segoe UI Emoji", 10, "bold"),background="#C6E2FF",foreground="white",rowheight=34,fieldbackground="#B4CDCD")
        self.style.map("Treeview",background=[("selected", "#6993f6")],foreground=[("selected", "#ffffff")])

        self.scrollbar = ttk.Scrollbar(frame_tree, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.tree_view = ttk.Treeview(frame_tree,columns=('codigo', 'nome', 'exame', 'data', 'horario', 'contato', 'especialista'),show="", yscrollcommand=self.scrollbar.set)
        self.tree_view.column('codigo', width=80, anchor=CENTER)
        self.tree_view.column('nome', width=200, anchor=CENTER)
        self.tree_view.column('exame', width=180, anchor=CENTER)
        self.tree_view.column('data', width=120, anchor=CENTER)
        self.tree_view.column('horario', width=100, anchor=CENTER)
        self.tree_view.column('contato', width=160, anchor=CENTER)
        self.tree_view.column('especialista', width=200, anchor=CENTER)
        
        Label(frame_header, text="CODIGO", bg="#ffffff", fg="black",font=("Segoe UI Semibold", 14)).place(x=33, y=8)
        self.imagem_logo_id = PhotoImage(file=pastaApp + "\\IMG\\img_id.png")
        Label(frame_header, image=self.imagem_logo_id,background="#ffffff").place(x=6, y=10)

        Label(frame_header, text="NOME", bg="#ffffff", fg="black",font=("Segoe UI Semibold", 14)).place(x=185, y=8)
        self.imagem_logo_nome = PhotoImage(file=pastaApp + "\\IMG\\img_cliente.png")
        Label(frame_header, image=self.imagem_logo_nome,background="#ffffff").place(x=155, y=10)
        
        Label(frame_header, text="EXAME", bg="#ffffff", fg="black",font=("Segoe UI Semibold", 14)).place(x=380, y=8)
        self.imagem_logo_exame = PhotoImage(file=pastaApp + "\\IMG\\img_exame.png")
        Label(frame_header, image=self.imagem_logo_exame,background="#ffffff").place(x=355, y=10)
        
        Label(frame_header, text="DATA", bg="#ffffff", fg="black",font=("Segoe UI Semibold", 14)).place(x=535, y=8)
        self.imagem_logo_data = PhotoImage(file=pastaApp + "\\IMG\\img_calendario.png")
        Label(frame_header, image=self.imagem_logo_data,background="#ffffff").place(x=509, y=10)
        
        Label(frame_header, text="HORARIO", bg="#ffffff", fg="black",font=("Segoe UI Semibold", 14)).place(x=635, y=8)
        self.imagem_logo_relogio = PhotoImage(file=pastaApp + "\\IMG\\img_relogio.png")
        Label(frame_header, image=self.imagem_logo_relogio,background="#ffffff").place(x=610, y=10)

        Label(frame_header, text="CONTATO", bg="#ffffff", fg="black",font=("Segoe UI Semibold", 14)).place(x=770, y=8)
        self.imagem_logo_telefone = PhotoImage(file=pastaApp + "\\IMG\\img_telefone.png")
        Label(frame_header, image=self.imagem_logo_telefone,background="#ffffff").place(x=745, y=10)
        
        Label(frame_header, text="ESPECIALISTA", fg="black", bg="#ffffff",font=("Segoe UI Semibold", 14)).place(x=938, y=8)
        self.imagem_logo_medico = PhotoImage(file=pastaApp + "\\IMG\\img_medico.png")
        Label(frame_header, image=self.imagem_logo_medico,background="#ffffff").place(x=914, y=10)
        
        self.tree_view.tag_configure("par", background="#f2f2f2")
        self.tree_view.tag_configure("impar", background="#ffffff")
        self.tree_view.tag_configure("passado", foreground="#EF2536") 
        self.tree_view.tag_configure("hoje", foreground="#20DD4C")     
        self.tree_view.tag_configure("futuro", foreground="#1171F8") 
        
        self.scrollbar.config(command=self.tree_view.yview)
        self.tree_view.pack(side=LEFT, fill=BOTH, expand=True)
        self.tree_view.bind("<Double-1>", self.janela_pesquisa)

        self.banco.conectar()
        self.tree_view.delete(*self.tree_view.get_children())
        codigo_sql = 'SELECT * FROM sys_lab_exames'
        self.banco.cursor.execute(codigo_sql)
        resultado_sql = self.banco.cursor.fetchall()
        for i, f in enumerate(resultado_sql):
            data = f[4]
            tag_data = self.definir_data_tag(data)
            tag_zebra = "par" if i % 2 == 0 else "impar"
            self.tree_view.insert("","end",id=f[0],text=f[0],values=(f[0], f[1], f[2], f[4], f[5], f[3], f[6], f[7]),tags=(tag_data,tag_zebra))

        self.frame_3 = Frame(self.toplevel,background="#2F3542")
        self.frame_3.place(x=0, y=0, width=1130, height=88)

        self.label_texto = Label(self.toplevel, text="EXAMES", foreground="white", background="#2F3542",font=("calibri", 20, "bold"))
        self.label_texto.place(x=25, y=20, width=200, height=20)

        self.botao_consulta_paciente = Button(self.toplevel, relief="flat",borderwidth=2, activebackground="#2f66ff", activeforeground="white" ,font=("arial 9 bold"),text="        PESQUISAR PACIENTE [F1]",background="#2f66ff",foreground="white", cursor="hand2", command=self.pesquisar_paciente)
        self.botao_consulta_paciente.place(x=495, y=58, width=188, height=30)
        self.imagem_logo_5 = PhotoImage(file=pastaApp + "\\IMG\\icon3.png")
        Label(self.toplevel, image=self.imagem_logo_5,background="#2f66ff").place(x=496, y=59)

        btn_close = Button(self.toplevel, text="X", bg="red", fg="white", cursor="hand2",command=self.toplevel.destroy, bd=0)
        btn_close.place(x=1090, y=5, width=25, height=20)
        
        self.entry_nome_cliente = Entry(self.toplevel, borderwidth=1,relief="solid", font=("calibri", 15))
        self.entry_nome_cliente.place(x=5, y=58, width=490, height=30)
        self.entry_nome_cliente.insert(0, "Buscar....")
        self.entry_nome_cliente.config(fg="gray")

        self.entry_nome_cliente.bind("<FocusIn>", self.entry_on)
        self.entry_nome_cliente.bind("<FocusOut>", self.entry_of)

        self.toplevel.bind("<Button-1>", self.start_move)
        self.toplevel.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = event.x_root - self.x
        y = event.y_root - self.y
        self.toplevel.geometry(f"+{x}+{y}")
    
    def filtrar(self, tipo):
        self.tree_view.delete(*self.tree_view.get_children())

        self.banco.cursor.execute('SELECT * FROM sys_lab_exames')
        dados = self.banco.cursor.fetchall()

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

        self.item_selecionado = False

    def definir_data_tag(self, data_str):
        hoje = datetime.now().date()
        try:
            data_exame = datetime.strptime(data_str, "%d/%m/%Y").date()
        except:
            return ""
        if data_exame < hoje:
            return "passado"
        elif data_exame == hoje:
            return "hoje"
        else:
            return "futuro"     

    def janela_pesquisa(self, event):
        item = self.tree_view.focus()
        if not item:
            return

        valores = self.tree_view.item(item, "values")
        
        self.janela_edicao = Toplevel(self.toplevel)
        self.janela_edicao.configure(background="#939393")
        self.janela_edicao.overrideredirect(True)
        central = CentralizadorDeJanelas()
        central.centralizar_toplevel(self.janela_edicao, 580, 300, self.toplevel)

        frame_funcao = Frame(self.janela_edicao,background="#D0D0D0")
        frame_funcao.place(x=10,y=222, width=560,height=50)

        frame = Frame(self.janela_edicao, background="#D0D0D0")
        frame.place(x=10, y=40, width=560, height=150)

        self.label_nome_paciente = Label(frame,text="NOME",foreground="black",background="#D0D0D0",font=("arial", 10, "bold"))
        self.label_nome_paciente.place(x=2, y=10, width=50, height=20)
        self.entry_nome_paciente = Entry(frame, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_nome_paciente.place(x=8, y=30, width=250, height=30)
        self.entry_nome_paciente.insert(0, valores[1])

        self.label_exame = Label(frame, text="EXAME", background="#D0D0D0", foreground="black", font=("arial", 10, "bold"))
        self.label_exame.place(x=270, y=10, width=60, height=20)
        self.combobox_1 = ttk.Combobox(frame,font=("calibri", 15),values=["Covid-19", "Hemograma", "Urina", "Sangue"])
        self.combobox_1.place(x=273, y=30, width=180, height=30)
        self.combobox_1.set("")
        self.combobox_1.insert(0, valores[2])

        self.label_contato = Label(frame, text="CONTATO", background="#D0D0D0", foreground="black", font=("arial", 10, "bold"))
        self.label_contato.place(x=305, y=60, width=80, height=20)
        self.entry_contato = Entry(frame, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_contato.bind("<KeyRelease>", lambda e: self.formatacao.formatar_telefone(self.entry_contato, e))
        self.entry_contato.place(x=315, y=80, width=155, height=30)
        self.entry_contato.insert(0, valores[5])

        self.label_data = Label(frame, text="DATA", foreground="black", background="#D0D0D0", font=("arial", 10, "bold"))
        self.label_data.place(x=180, y=60, width=60, height=20)
        self.entry_data = Entry(frame, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_data.bind("<KeyRelease>", lambda e: self.formatacao.formatar_data(self.entry_data, e))
        self.entry_data.place(x=190, y=80, width=110, height=30)
        self.entry_data.insert(0, valores[3])

        self.label_horario = Label(frame, text="HORARIO", foreground="black", background="#D0D0D0", font=("arial", 10, "bold"))
        self.label_horario.place(x=470, y=60, width=85, height=20)
        self.entry_horario = Entry(frame, borderwidth=1, relief="solid", font=("calibri", 15))
        self.entry_horario.bind("<KeyRelease>", lambda e: self.formatacao.formatar_horario(self.entry_horario, e))
        self.entry_horario.place(x=480, y=80, width=76, height=30)
        self.entry_horario.insert(0, valores[4])

        self.label_especialista = Label(frame, text="ESPECIALISTA", foreground="black", background="#D0D0D0", font=("arial", 10, "bold"))
        self.label_especialista.place(x=5, y=60, width=100, height=20)
        self.combobox_2 = ttk.Combobox(frame,font=("calibri", 15),values=["Dr.Miguel", "Dr.André", "Dra.Rafaela", "Dra.Carol"])
        self.combobox_2.place(x=8, y=80, width=170, height=30)
        self.combobox_2.insert(0, valores[6])

        self.label_codigo = Label(frame, text="CODIGO", foreground="black",background="#D0D0D0", font=("arial", 10, "bold"))
        self.label_codigo.place(x=465, y=10, width=85, height=20)
        self.entry_codigo = Entry(frame, borderwidth=1, relief="solid",font=("calibri", 15))
        self.entry_codigo.place(x=480, y=30, width=75, height=30)
        self.entry_codigo.insert(0, valores[0])

        Label(self.janela_edicao, text="Informações do exame", bg="#939393", fg="black",font=("Segoe UI Semibold", 14)).place(x=30, y=8)
        self.imagem_logo_exam = PhotoImage(file=pastaApp + "\\IMG\\img_exam.png")
        Label(self.janela_edicao, image=self.imagem_logo_exam,background="#939393").place(x=6, y=10)

        Label(self.janela_edicao, text="Ações", bg="#939393", fg="black",font=("Segoe UI Semibold", 14)).place(x=30, y=191)
        self.imagem_logo_acao = PhotoImage(file=pastaApp + "\\IMG\\img_configuracao.png")
        Label(self.janela_edicao, image=self.imagem_logo_acao,background="#939393").place(x=6, y=195)

        btn_close = Button(self.janela_edicao, text="X", bg="red", fg="white", cursor="hand2",command=self.janela_edicao.destroy, bd=0)
        btn_close.place(x=550, y=5, width=25, height=20)

        self.janela_edicao.bind("<Button-1>", self.start_move_1)
        self.janela_edicao.bind("<B1-Motion>", self.do_move_1)

        self.botao_atualizar = Button(self.janela_edicao, relief="solid",borderwidth=1, font=("arial 9 bold"),text="        ATUALIZAR PACIENTE [F1]",background="#FDFFFF",foreground="black",activebackground="#E8F0F1", cursor="hand2", command=self.atualizar_paciente)
        self.botao_atualizar.place(x=22, y=230, width=180, height=35)
        self.imagem_logo_3 = PhotoImage(file=pastaApp + "\\IMG\\icon4.png")
        Label(self.janela_edicao, image=self.imagem_logo_3,background="#FDFFFF").place(x=23, y=231)

        self.botao_excluir = Button(self.janela_edicao, relief="solid",borderwidth=1, font=("arial 9 bold"),text="     EXCLUIR PACIENTE [F2]",background="#FDFFFF",foreground="black",activebackground="#E8F0F1", cursor="hand2", command=self.excluir_paciente)
        self.botao_excluir.place(x=208, y=230, width=175, height=35)
        self.imagem_logo_2 = PhotoImage(file=pastaApp + "\\IMG\\icon2.png")
        Label(self.janela_edicao, image=self.imagem_logo_2,background="#FDFFFF").place(x=209, y=231)

        self.botao_pdf = Button(self.janela_edicao, text="      GERAR PDF [F3]", borderwidth=1, relief="solid", background="#FDFFFF",foreground="black", font=("arial 9 bold"),activebackground="#E8F0F1", cursor="hand2", command=self.criar_pdf)
        self.botao_pdf.place(x=388, y=230, width=165, height=35)
        self.imagem_logo_1 = PhotoImage(file=pastaApp + "\\IMG\\imgpdf.png")
        Label(self.janela_edicao, image=self.imagem_logo_1,background="#FDFFFF").place(x=389, y=231)

        self.item_selecionado = False

    def start_move_1(self, event):
            self.x = event.x
            self.y = event.y

    def do_move_1(self, event):
            x = event.x_root - self.x
            y = event.y_root - self.y
            self.janela_edicao.geometry(f"+{x}+{y}")

    def duploclick(self,event):
        self.tree_view.selection()
        for n in self.tree_view.selection():
            nome,cpf, = self.tree_view.item(n, 'values')
            self.entry_nome_cliente.insert(END,nome)
            self.entry_codigo.insert(END,cpf)

    def atualizar_paciente(self):
        self.banco.conectar()
        nome_paciente = self.entry_nome_paciente.get().strip()
        exame = self.combobox_1.get().strip()
        contato = self.entry_contato.get().strip()
        data = self.entry_data.get().strip()
        horario = self.entry_horario.get().strip()
        especialista = self.combobox_2.get().strip()
        codigo = self.entry_codigo.get().strip()
        if nome_paciente == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto="Selecione um paciente\n para realizar a ação!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja atualizar o exame?",cor_fundo="#A9A9A9",cor_texto="black")
            if resposta:
                codigo_sql = "UPDATE sys_lab_exames SET nome=%s, exame=%s,contato=%s, data=%s, horario=%s, especialista=%s WHERE id=%s"
                valores_sql = (nome_paciente, exame, contato, data, horario,especialista, codigo)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem",texto="Dados atualizados!",cor_fundo="#A9A9A9",cor_texto="black",caminho_img=pastaApp + "\\IMG\\sucesso.png")
                #self.janela_edicao.destroy()
                #self.tree_view.delete(*self.tree_view.get_children())
                codigo_sql_select = 'SELECT * FROM sys_lab_exames'
                self.banco.cursor.execute(codigo_sql_select)
                resultado_sql = self.banco.cursor.fetchall()
                #for i, item in enumerate(resultado_sql):
                    #if i % 2 == 0: 
                        #tag = "par" 
                    #else:
                        #tag = "impar"
                    #self.tree_view.insert("","end",values=(item[0],item[1],item[2],item[4],item[5],item[3],item[6],item[7]),tags=(tag,))
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro",texto=f"Erro ao atualizar ....{e}",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")
        finally:
            self.banco.conexao.close()

    def criar_pdf(self):
        self.banco.conectar()
        nome_pdf = self.entry_nome_paciente.get().strip()
        exame_pdf = self.combobox_1.get().strip()
        contato_pdf = self.entry_contato.get().strip()
        horario_pdf = self.entry_horario.get().strip()
        especialista_pdf = self.combobox_2.get().strip()
        data_pdf = self.entry_data.get().strip()
        if nome_pdf == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto="O recibo não pode ser gerado\n por falta de informações!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
            return
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("Arquivo PDF", "*.pdf")],title="Salvar relatório de exames")
        if not caminho_arquivo:
            return

        self.canvas = canvas.Canvas(caminho_arquivo)

        self.canvas.drawImage(pastaApp + "\\IMG\\logo_pdf.png", 50, 730, width=80, height=80)
        self.canvas.setFont("Helvetica-Bold", 18)
        self.canvas.drawString(150, 770, "Laboratório São Bento")

        self.canvas.setFont("Helvetica", 12)
        self.canvas.drawString(150, 755,"Rua 14 de Fevereiro, 780, Vila Guaporé, Pontes e Lacerda MT")
        self.canvas.drawString(150, 740,"Tel: 3266-1946 | WhatsApp: (65) 9 8121-7628")

        self.canvas.line(30, 720, 570, 720)

        self.canvas.setFillColorRGB(0.18, 0.52, 0.76)
        self.canvas.rect(1, 590, 850, 30, fill=1, stroke=0)
        self.canvas.setFillColorRGB(1, 1, 1)
        self.canvas.setFont("Helvetica-Bold", 16)
        self.canvas.drawCentredString(290, 595, "DADOS DO EXAME")

        self.canvas.setFillColorRGB(0, 0, 0)
        y = 560

        campos = ["Nome:", "Exame:", "Contato:", "Horário:","Data da Consulta:", "Especialista:"]
        valores = [nome_pdf, exame_pdf, contato_pdf, horario_pdf, data_pdf, especialista_pdf]

        for i, campo in enumerate(campos):
            altura = y - i * 25
            self.canvas.setFont("Helvetica-Bold", 12)
            self.canvas.drawString(25, altura, campo)
            self.canvas.setFont("Helvetica", 12)
            self.canvas.drawString(150, altura, valores[i])
            self.canvas.line(25, altura - 5, 550, altura - 5)

        self.canvas.line(30, 60, 570, 60)
        self.canvas.setFont("Helvetica-Oblique", 10)
        self.canvas.drawString(
            45, 45,
            "Assinatura do Cliente: _____________________________________"
            "                                        Data: ___/___/____")
        self.canvas.drawRightString(570, 30,"SysLab - Sistema de Gestão Laboratorial v1.0")
        self.canvas.showPage()
        self.canvas.save()

    def pesquisar_paciente(self):
        self.banco.conectar()
        consulta=self.entry_nome_cliente.get().strip()
        if  consulta == "" or "Buscar....":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="Informe o nome para pesquisa!", cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
            #return 
        try:
            self.tree_view.delete(*self.tree_view.get_children())
            codigo_sql = 'SELECT * FROM sys_lab_exames WHERE nome LIKE %s ORDER BY id'
            valores_sql=('%' + consulta + '%',)
            self.banco.cursor.execute(codigo_sql, valores_sql)
            resultado_sql = self.banco.cursor.fetchall()
            if len(resultado_sql) > 0:
                for i, item in enumerate(resultado_sql):
                    tag = "par" if i % 2 == 0 else "impar"
                    self.tree_view.insert("","end",values=(item[0], item[1], item[2], item[4], item[5], item[3], item[6], item[7]),tags=(tag,))
            else:
                self.mensagem.alerta_erro_sucesso(titulo="Alerta", texto="A busca não obteve resultado!",cor_fundo="#A9A9A9", caminho_img="IMG/alerta.png")
                self.entry_nome_cliente.delete(0,END)
        except  Exception as e:
                self.mensagem.alerta_erro_sucesso(titulo="Erro", texto=f"Erro ao editar....{e}", cor_fundo="#A9A9A9", caminho_img="IMG/erro.png")
        finally:
            self.banco.conexao.close()

    def excluir_paciente(self):
        self.banco.conectar()
        codigo = self.entry_codigo.get().strip()
        if codigo == "":
            self.mensagem.alerta_erro_sucesso(titulo="Alerta",texto="Selecione um exame para excluir!",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\alerta.png")
            return
        try:
            resposta = self.mensagem.perguntar(titulo="Confirmação",texto="Deseja excluir o exame?",cor_fundo="#A9A9A9",cor_texto="black")
            if resposta:
                codigo_sql = "DELETE FROM sys_lab_exames WHERE id=%s"
                valores_sql = (codigo,)
                self.banco.cursor.execute(codigo_sql, valores_sql)
                self.banco.conexao.commit()
                self.mensagem.alerta_erro_sucesso(titulo="Mensagem",texto="Exame excluído!",cor_fundo="#A9A9A9",cor_texto="black",caminho_img=pastaApp + "\\IMG\\sucesso.png")
                self.janela_edicao.destroy()
                self.tree_view.delete(*self.tree_view.get_children())
                codigo_sql_select = 'SELECT * FROM sys_lab_exames'
                self.banco.cursor.execute(codigo_sql_select)
                resultado_sql = self.banco.cursor.fetchall()
                for i, item in enumerate(resultado_sql):
                    tag = "par" if i % 2 == 0 else "impar"
                    self.tree_view.insert("","end",values=(item[0],item[1],item[2],item[4],item[5],item[3],item[6],item[7]),tags=(tag,))
        except Exception as e:
            self.mensagem.alerta_erro_sucesso(titulo="Erro",texto=f"Erro ao deletar....{e}",cor_fundo="#A9A9A9",caminho_img=pastaApp + "\\IMG\\erro.png")
        finally:
            self.banco.conexao.close()
            