"""
========================================================
   Sistema: SysLab
   Desenvolvedor: Rogério Gomes Figueiredo
   Versão: 1.0
   Contato: rogerio_bk@outlook.com
   Telefone:
   Descrição: Sistema de gestão para laboratórios.
========================================================
"""

from tkinter import *
#from telas.tela_login import TelaLogin
from telas.tela_principal import TelaPrincipal

def main():
    root = Tk()
    TelaPrincipal(root)
    #TelaLogin(root)
    root.mainloop()
if __name__ == "__main__":
    main()
    
