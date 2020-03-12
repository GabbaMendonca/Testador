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
        print("\n", texto, "\n")
    return input("Escreva <<< ")

def entrada_senha(texto=None):
    if texto:
        print("\n", texto, "\n")
    return getpass(prompt="Escreva <<< ")


# ----- MENUS -----

def menu_server_testes():
    return entrada(
        """
        Escolha :
        (0) >>> Assimir o terminal 
        (1) >>> ssh 
        (2) >>> telnet
        (3) >>> ping
        """
    )

def menu_ssh_alcatel():
    return entrada(
        """
        Escolha :
        (1) >>> Acessar o router 
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
        (0) >>> Assimir o terminal 
        (1) >>> Rodar testes 
        """
    )