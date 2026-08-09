from tkinter import *
from PIL import Image, ImageTk

class CaixaMensagemPersonalizada:
    def tela_mensagem(self, titulo, largura, altura, cor_fundo):
        tela_mensagem = Toplevel()
        tela_mensagem.overrideredirect(1)
        tela_mensagem.title(titulo)
        tela_mensagem.configure(bg=cor_fundo)
        tela_mensagem.resizable(False, False)
        x = (tela_mensagem.winfo_screenwidth() // 2) - (largura // 2)
        y = (tela_mensagem.winfo_screenheight() // 2) - (altura // 2)
        tela_mensagem.geometry(f"{largura}x{altura}+{x}+{y}")
        return tela_mensagem

    def carregar_imagem(self, caminho, tamanho, container, cor_fundo):
        try:
            imagem = Image.open(caminho)
            imagem = imagem.resize(tamanho)
            img_tk = ImageTk.PhotoImage(imagem)
            label_img = Label(container, image=img_tk, bg=cor_fundo)
            label_img.image = img_tk
            label_img.pack(pady=(10, 0))
        except Exception as e:
            print("Erro ao carregar imagem:", e)

    def criar_frame_destaque(self, parent, cor_fundo, borda=3):
        frame = Frame(parent, bg=cor_fundo, relief="ridge", borderwidth=borda)
        frame.pack(expand=True, fill="both", padx=2, pady=2)
        return frame

    def alerta_erro_sucesso(self, titulo="", texto="", cor_fundo="white", cor_texto="black", caminho_img=""):
        def sim(): tela_mensagem.destroy()

        tela_mensagem = self.tela_mensagem(titulo, 230, 160, cor_fundo)
        frame = self.criar_frame_destaque(tela_mensagem, cor_fundo)

        self.carregar_imagem(caminho_img, (40, 40), frame, cor_fundo)
        Label(frame, text=texto, bg=cor_fundo, fg=cor_texto, font=("Arial", 10), wraplength=220, justify=CENTER).pack(pady=10, padx=10)

        frame_botoes = Frame(frame, bg=cor_fundo)
        frame_botoes.pack(pady=(0, 10))
        Button(frame_botoes, text="OK", width=10, bg="#3CB371", command=sim).pack()

        tela_mensagem.transient()
        tela_mensagem.grab_set()
        tela_mensagem.wait_window()

    def perguntar(self, titulo="Confirmação", texto="Deseja continuar?", cor_fundo="white", cor_texto="white", caminho_img="IMG/question.png"):
        resultado = {"resposta": None}

        def resposta_sim():
            resultado["resposta"] = True
            tela_mensagem.destroy()

        def resposta_nao():
            resultado["resposta"] = False
            tela_mensagem.destroy()

        tela_mensagem = self.tela_mensagem(titulo, 230, 140, cor_fundo)
        frame = self.criar_frame_destaque(tela_mensagem, cor_fundo, borda=2)

        self.carregar_imagem(caminho_img, (40, 40), frame, cor_fundo)
        Label(frame, text=texto, bg=cor_fundo, fg=cor_texto, font=("Arial", 10), wraplength=220, justify=CENTER).pack(pady=10, padx=10)

        Button(frame, text="SIM ", width=10, bg="green", foreground="white", command=resposta_sim).pack(side="left", padx=15)
        Button(frame, text="NÃO ", width=10, bg="red", foreground="white", command=resposta_nao).pack(side="right", padx=15)

        tela_mensagem.transient()
        tela_mensagem.grab_set()
        tela_mensagem.wait_window()

        return resultado["resposta"]
