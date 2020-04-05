import pickle #modulo pickle

#dicionário
LOGIN = {}

IP_SERVER_TESTES = {}

# ----- MANIPULR ARQUIVOS EXTERNOS -----
def gravar_dicionario(dicionario, nome_do_arquivo:str):
    try:    
        arq = open(nome_do_arquivo + '.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
    except:
        return False
    else:
        pickle.dump(dicionario,arq) #Grava uma stream do objeto "dic" para o arquivo.
        arq.close() #fechar o arquivo


def ler_dicionario(nome:str):
    try:
        arq = open(nome + '.txt','rb') #abrir o arquivo para leitura - o "b" significa que o arquivo é binário
    except FileNotFoundError:
        return False
    else:    
        dic = pickle.load(arq) #Ler a stream a partir do arquivo e reconstroi o objeto original.
        arq.close() #fechar o arquivo
        return dic #retorna o conteúdo do dicionário
    
    

# ----- MANIPULR DADOS -----
# --- IP SERVER TESTES ---
def criar_ip_server_teste(num_server, ip_sever):
    """
    Obtem o IP de server de testes do usuario e adiciona em um dicionario
    """

    IP_SERVER_TESTES[str(num_server)] = {
        'server': num_server, 'ip': ip_sever}

def ler_ip_server_testes():
    """
    Mostar a lista de servers do dicionario.
    """

    lista = []
    for x in IP_SERVER_TESTES:
        lista.append("Server : {0} - IP do Server : {1}".format(
            str(IP_SERVER_TESTES[x]['server']), IP_SERVER_TESTES[x]['ip']))

    return lista

def atualizar_ip_server_testes(num_server, ip_server):
    """
    Atualiza o IP de um server no dicionario.
    """

    criar_ip_server_teste(num_server, ip_server)

def deletar_ip_server_testes(num_server):
    """
    Deleta o IP de um server no dicionario.
    """

    for x in IP_SERVER_TESTES:
        if int(x) >= num_server:
            y = int(x)
            y = y + 1
            z = str(y)
            IP_SERVER_TESTES[x]['ip'] = IP_SERVER_TESTES[z]['ip']
            if y == len(IP_SERVER_TESTES):
                IP_SERVER_TESTES.pop(str(y))
                break

def carregar_ip_server_testes():
    """
    Tenta carregar o arquivo externo com o ip de server e retorna a validacao
    """

    IP_SERVER_TESTES = ler_dicionario('ip_server')

    if IP_SERVER_TESTES:
        return True
    else:
        return False

def gravar_ip_server_teste():
    """
    Grava o dicionario em arquivo externo
    """

    gravar_dicionario(
        dicionario=IP_SERVER_TESTES, nome_do_arquivo='ip_server')

# --- LOGIN E SENHA ---
def criar_login_e_senha(login, senha):
    """
    Obtem o login e senha do usuario e adiciona em um dicionario
    """

    posicao = len(LOGIN)
    LOGIN[str(posicao)] = {'login': login, 'senha': senha}

def ler_login_e_senha():
    """
    Mostar a lista de logins do dicionario.
    """

    lista = []
    for x in LOGIN:
        lista.append("Login : {0}".format(str(LOGIN[x]['login'])))

    return lista

def atualizar_login_e_senhas(posicao, login, senha):
    """
    Atualiza o IP de um server no dicionario.
    """

    LOGIN[str(posicao)] = {'login': login, 'senha': senha}

def deletar_login_e_senha(posicao):
    """
    Deleta o IP de um server no dicionario.
    """

    for x in LOGIN:
        if int(x) >= posicao:
            y = int(x)
            y = y + 1
            z = str(y)
            if y < len(LOGIN):
                LOGIN[x]['login'] = LOGIN[z]['login']
                LOGIN[x]['senha'] = LOGIN[z]['senha']
            else:
                y = y - 1
                LOGIN.pop(str(y))
                break

def carregar_login_e_senha():
    """
    Tenta carregar o arquivo externo com o ip de server e retorna a validacao
    """
    
    LOGIN = ler_dicionario('login')

    if LOGIN:
        return True
    else:
        return False

def gravar_login_e_senha():
    """
    Grava o dicionario em arquivo externo
    """

    gravar_dicionario(
        dicionario=LOGIN, nome_do_arquivo='login')
