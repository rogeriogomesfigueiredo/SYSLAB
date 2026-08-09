from tkinter import *

class CentralizadorDeJanelas:
    def centralizar_janela(self, root, largura, altura):
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    def centralizar_toplevel(self, toplevel, largura, altura, janela_pai):
        janela_pai.update_idletasks()
        x_pai = janela_pai.winfo_x()
        y_pai = janela_pai.winfo_y()
        largura_pai = janela_pai.winfo_width()
        altura_pai = janela_pai.winfo_height()

        pos_x = x_pai + (largura_pai // 2) - (largura // 2)
        pos_y = y_pai + (altura_pai // 2) - (altura // 2)

        toplevel.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
