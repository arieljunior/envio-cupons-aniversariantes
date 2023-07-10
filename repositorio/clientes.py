from entidades.cliente import Cliente 
import os
import dotenv

dotenv.load_dotenv()
CAMINHO_ARQUIVO_DADOS = os.getenv("CAMINHO_DADOS_ARQUIVO")

def get_todos_clientes() -> list:
    clientes = []
    with open(CAMINHO_ARQUIVO_DADOS, 'r', encoding="utf8") as arquivo:
        linha_atual = 0
        for linha in arquivo:
            if linha_atual == 0:
                linha_atual += 1
            else:
                lista_valores = linha.split(",")
                cliente = Cliente(
                    nome_completo=lista_valores[0],
                    data_nascimento=lista_valores[1],
                    email=lista_valores[2],
                    data_criacao=lista_valores[3].replace("\n", "")
                )
                clientes.append(cliente)
    return clientes