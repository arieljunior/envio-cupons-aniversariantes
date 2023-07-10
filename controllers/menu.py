import repositorio.clientes as clientes_repositorio

def iniciar_menu_principal():
    while True:
        print("1 - Consultar clientes\n2 - Cadastrar cliente\n3 - Enviar cupons via email aos clientes aniversariantes\n4 - Sair")
        opcao_escolhida = input("Digite uma opção: ")

        match opcao_escolhida:
            case '1':
                print("CONSULTAR CLIENTES")
                iniciar_submenu_consulta_clientes()
            case '2':
                print("CADASTRAR CLIENTE")
            case '3':
                print("ENVIAR CUPONS VIA EMAIL")
            case '4':
                break
            case other:
                print("Opção inválida")

def iniciar_submenu_consulta_clientes():
    while True:
        print("1 - Todos\n2 - Aniversariantes\n3 - Aniversariantes de um mês específico\n4 - Voltar para o menu principal")
        opcao_escolhida = input("Digite uma opção: ")
        match opcao_escolhida:
            case '1':
                print("CONSULTAR TODOS OS CLIENTES")
                mostrar_todos_clientes()
                break
            case '2':
                print("CONSULTAR CLIENTES ANIVERSARIANTES")
                break
            case '3':
                print("CONSULTAR CLIENTES ANIVERSARIANTES DE UM MÊS ESPECÍFICO")
                break
            case '4':
                break
            case other:
                print("Opção inválida")

def mostrar_todos_clientes():
    clientes = clientes_repositorio.get_todos_clientes()
    for cliente in clientes:
        print(f"NOME: {cliente.nome_completo}\nDATA NASCIMENTO: {cliente.data_nascimento}\nEMAIL: {cliente.email}\nDATA CRIACAO: {cliente.data_criacao}\n")