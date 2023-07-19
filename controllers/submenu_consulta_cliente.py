import repositorio.clientes as clientes_repositorio
from entidades.cliente import Cliente

def iniciar_submenu_consulta_clientes():
    print("\nCONSULTAR CLIENTES\n")
    while True:
        print("1 - Todos\n2 - Aniversariantes\n3 - Aniversariantes de um mês específico\n4 - Voltar para o menu principal")
        opcao_escolhida = input("Digite uma opção: ")
        match opcao_escolhida:
            case '1':
                mostrar_todos_clientes()
                break
            case '2':
                mostrar_clientes_aniversariantes()
                break
            case '3':
                mostrar_clientes_por_mes_aniversario()
                break
            case '4':
                break
            case other:
                print("Opção inválida")

def mostrar_todos_clientes():
    print("\nCONSULTAR TODOS OS CLIENTES\n")
    clientes = clientes_repositorio.get_todos_clientes()
    Cliente.mostrar_clientes(clientes)

def mostrar_clientes_aniversariantes():
    print("\nCONSULTAR CLIENTES ANIVERSARIANTES\n")
    aniversariantes = clientes_repositorio.get_clientes_aniversariantes()
    if len(aniversariantes) > 0:
        Cliente.mostrar_clientes(aniversariantes)
    else:
        print("Ninguém faz aniversário hoje")

def mostrar_clientes_por_mes_aniversario():
    print("\nCONSULTAR CLIENTES ANIVERSARIANTES DE UM MÊS ESPECÍFICO\n")
    mes = int(input("Digite o número do mês (1-12):"))

    aniversariantes = clientes_repositorio.get_clientes_por_mes_aniversario(mes)

    if len(aniversariantes) > 0:
        Cliente.mostrar_clientes(aniversariantes)
    else:
        print("Ninguém faz aniversário neste mês")
   