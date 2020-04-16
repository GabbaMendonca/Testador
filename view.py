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

# ----- TELA DE BOAS VINDAS -----


class ViewBoasVindas():
    @staticmethod
    def tela_de_boas_vindas():
        imprimir(
"""
-------------------------------------------------
|    ### Bem - Vindo ! ###                      |
|                                               |
|    Este é o Testador de Circuitos !           |
-------------------------------------------------
"""
        )
        
    @staticmethod
    def tela_de_conclusao_boas_vindas():
        imprimir(
"""
-------------------------------------------------
|    OK - Estamos preparados para começar !     |
-------------------------------------------------
"""
        )
        

# ----- SERVER -----


class ViewServer():
    @staticmethod
    def primeiro_acesso_server():
        return entrada(
"""
-------------------------------------------------
|    ### Configurações ! ###                    |
|                                               |
|    Primeiro vamos fazer algumas               | 
|    configurações basicas !                    |
|                                               |
|    Digite e IP do Server para testes !        |
-------------------------------------------------            
"""
            )


# ----- LOGIN -----


class ViewLogin():
    @staticmethod
    def login_user():
        return entrada(
"""
-------------------------------------------------
|    ### Configurações ! ###                    |
|                                               |
|                                               |
|    Agora digite o seu usuario (Login OI) !    |
-------------------------------------------------            
"""
        )

    @staticmethod
    def login_senha():
        return entrada(
"""
-------------------------------------------------
|    ### Configurações ! ###                    |
|                                               |
|                                               |
|    Agora digite a sua senha !                 |
-------------------------------------------------         
"""
        )
        
        
# ----- MENU INICIAL -----
class ViewMenuInicial():
    @staticmethod
    def menu_inicial():
        return entrada(
"""
-------------------------------------------------
|    ### Menu Inicial ! ###                     |
|                                               |
|    Escolha :                                  | 
|    (1) >>> Iniciar                            |
|    (9) >>> Configurações                      |
|    ---                                        |
|    (0) <<< Fechar                             |
-------------------------------------------------         
"""            
        )


    @staticmethod
    def modo_terminal():
        return entrada('Habilitar terminal simulado ? [Enter/n]')
    


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











    
