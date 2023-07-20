from calendar import isleap
from datetime import datetime
import utils.tabela as tabela
from string import Template
from utils.get_env import get_env
from dateutil.relativedelta import relativedelta

class Cliente():
    def __init__(self, nome_completo: str, data_nascimento: str, email: str, data_criacao: str) -> None:
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.data_criacao = data_criacao
    
    def eh_ano_bissexto(self):
        ano_atual = datetime.now().year
        return isleap(ano_atual) == False
    
    def faz_aniversario_ano_bissexto(self):
        dia, mes = self.data_nascimento.split("/")[:2]
        return dia == "29" and mes == "02"

    def get_dia_mes_aniversario(self) -> dict["dia": str, "mes": str, "ano": str]:
        dia, mes = self.data_nascimento.split("/")[:2]

        if self.eh_ano_bissexto() and self.faz_aniversario_ano_bissexto():
            dia = "28"

        data = {
            "dia": int(dia),
            "mes": int(mes)
        }
        return data
    
    def get_primeiro_nome(self) -> str:
        return self.nome_completo.split(" ")[0]

    def gerar_cupom_desconto(self) -> str:
        data_anterior = datetime.strptime(self.data_criacao, "%d/%m/%Y")
        hoje = datetime.today()

        diferenca = relativedelta(hoje, data_anterior)

        desconto = "30"
        if diferenca.years <= 1:
            desconto = "10"
        elif diferenca.years == 2:
            desconto = "20"

        primeiro_nome = self.get_primeiro_nome()
        return f"{primeiro_nome.upper()}{desconto}"

    def montar_objeto_email_aniversario(self):
        primeiro_nome = self.get_primeiro_nome()
        
        with open(get_env("CAMINHO_TEMPLATE_EMAIL"), "r", encoding="utf8") as arquivo_template:
            template_email = Template(arquivo_template.read())

        cupom_gerado = self.gerar_cupom_desconto()
        conteudo = template_email.substitute(
            NOME=primeiro_nome, 
            NOME_EMPRESA=get_env("NOME_EMPRESA"),
            CUPOM=cupom_gerado
        )
        return {
            "email": self.email,
            "mensagem": conteudo,
            "titulo_email": f"Feliz aniversário, {primeiro_nome}"
        }
    
    @staticmethod
    def mostrar_clientes(clientes: list) -> None:
        largura = 20
        cabecalho = tabela.montar_linha(
            ["NOME COMPLETO", "DATA NASCIMENTO", "EMAIL", "CLIENTE DESDE"], 
            eh_cabecalho=True, 
            largura_coluna=largura
        )
        print(cabecalho)
        contador = 0
        for cliente in clientes:
            linha = tabela.montar_linha(
                [cliente.nome_completo, cliente.data_nascimento, cliente.email, cliente.data_criacao],
                largura_coluna=largura
            )
            print(linha)
            contador +=1
            if contador == len(clientes):
                print("-" * len(linha))

