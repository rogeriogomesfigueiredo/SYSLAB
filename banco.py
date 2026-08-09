import mysql.connector

class BancoDeDados:
    def __init__(self, arquivo_config="config_ip.txt"):
        self.arquivo_configuracao = arquivo_config
        self.ip = self.ler_ip()
        self.conexao = None
        self.cursor = None

    def ler_ip(self):
        with open(self.arquivo_configuracao, "r") as f:
            return f.read().strip()

    def conectar(self, apenas_testar=False):
        try:
            conexao = mysql.connector.connect(host=self.ip,user="root",password="32591645",database="sys_lab",connect_timeout=1)
            if apenas_testar == True:
                conexao.close()
                return "Ativo"
            self.conexao = conexao
            self.cursor = self.conexao.cursor()
            return "Ativo"
        except Exception as e:
            print(f"Erro na conexão: {e}")
            return "Inativo"