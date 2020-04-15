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
        # print(texto)
        print("\n", texto ,"\n")
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
    
    
# ----- MENU INICIAL -----

def modo_terminal():
    return entrada('Habilitar terminal simulado ? [Enter/n]')

def menu_inicial():
    return entrada(
        """
        Bem-Vindo ao testador de Circuitos!

        Escolha :
        (1) >>> Iniciar
        (9) >>> Configurações
        ---
        (0) <<< Fechar
        """
    )


# ----- SERVER -----

    
def menu_configuracores():
    return entrada(
        """
        ### Configuraçẽs ###

        Escolha :
        (1) >>> Trocar IP do Server de testes
        (2) >>> Trocar senha 1
        (3) >>> Trocar senha 2
        ---
        (0) <<< Voltar
        """
    )


# ----- SERVER -----


class ViewServer():
    @staticmethod
    def server_ip():
        return entrada('Digite ip de server de testes')

    @staticmethod
    def server_nome():
        return entrada('Digite o server de testes')
    
    @staticmethod
    def imprimir_server():
        ...


# ----- LOGIN -----


class ViewLogin():
    @staticmethod
    def login_user():
        return entrada('Digite seu login')

    @staticmethod
    def login_senha():
        return entrada('Digite sua senha')


# ----- TELE DE BOAS VINDAS -----


class ViewBoasVindas():
    @staticmethod
    def tela_de_boas_vindas():
        return entrada(
            """
            ### Bem - Vindo ! ###
            """
        )
    
    
