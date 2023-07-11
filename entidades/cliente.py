class Cliente():
    def __init__(self, nome_completo: str, data_nascimento: str, email: str, data_criacao: str) -> None:
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.data_criacao = data_criacao
    
    def get_data_nascimento(self) -> dict["dia": str, "mes": str, "ano": str]:
        lista_data = self.data_nascimento.split("/")
        data = {
            "dia": int(lista_data[0]),
            "mes": int(lista_data[1]),
            "ano": int(lista_data[2])
        }
        return data
    
    @staticmethod
    def mostrar_clientes(clientes: list) -> None:
        for cliente in clientes:
            print(f"NOME: {cliente.nome_completo}\nDATA NASCIMENTO: {cliente.data_nascimento}\nEMAIL: {cliente.email}\nDATA CRIACAO: {cliente.data_criacao}\n")
