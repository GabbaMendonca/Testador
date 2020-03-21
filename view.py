from getpass import getpass

def imprimir(imprimir):
    print(imprimir)

def ter_imprimir(imprimir):
    if imprimir:
        for frases in imprimir[2:-1].split('\\r\\n'):
            print(frases)
    else:
        print("Comando retornou vazio !!!")

def entrada(texto=None):
    if texto:
        print(texto)
        # print("\n", texto, "\n")
    return input("Escreva <<< ")

def entrada_senha(texto=None):
    if texto:
        print("\n", texto, "\n")
    return getpass(prompt="Escreva <<< ")

def cadastrar_ip_server_testes():
    return entrada(
        """
        Por favor insira o ip do server de teste.
        """
    )


# ----- MENUS -----

def menu_server_testes():
    return entrada(
        """

        Escolha :
        (1) >>> ssh 
        (2) >>> telnet
        ---
        (9) >>> Assimir o terminal 
        (0) <<< Fechar
        """
    )

def menu_ssh_alcatel():
    return entrada(
        """

        Escolha :
        (1) >>> Pingar o circuito 
        (2) >>> Acessar o router 
        (3) >>> Ver BGP 
        ---
        (9) >>> Assimir o terminal 
        (0) <<< logout/sair
        """
    )

def menu_nao_tem():
    return entrada(
        """
        Funcoes ainda nao desenviolvidas !
        """
    )

def menu_router_alcatel():
    return entrada(
        """
        Escolha :
        (1) >>> Rodar tdos os testes
        ---
        (9) >>> Assimir o terminal 
        (0) <<< logout/sair
        """
    )