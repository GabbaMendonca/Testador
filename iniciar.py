import dicionario
from view import *
from terminal import Terminal


# ----- SERVER -----


def novo_server():
    server = dicionario.ler('server')

    if not server:
        return False

    num_server = (len(server) + 1)
    ip = ViewServer.primeiro_acesso_server()
    dicionario.adicionar('server', num_server, ip)


def carregar_server():
    server = dicionario.ler('server')

    if not server:
        ip = ViewServer.primeiro_acesso_server()
        dicionario.adicionar('server', '1', ip)
        return dicionario.ler('server')

    return server


def atulizar_server():
    server = ViewServer.server_nome()
    ip = ViewServer.server_nome()
    dicionario.atualizar('server', server, ip)


def deletar_server():
    server = ViewServer.server_nome()
    dicionario.deletar('server', server)


# ----- LOGIN -----


def novo_login():
    login = dicionario.ler('login')

    if not login:
        return False

    login = ViewLogin.login_user()
    senha = ViewLogin.login_senha()
    dicionario.adicionar('login', login, senha)


def carregar_login():
    login = dicionario.ler('login')

    if not login:
        login = ViewLogin.login_user()
        senha = ViewLogin.login_senha()
        dicionario.adicionar('login', login, senha)
        return dicionario.ler('login')
    
    return login


def atulizar_login():
    login = ViewLogin.login_user()
    senha = ViewLogin.login_senha()
    dicionario.adicionar('login', login, senha)


def deletar_login():
    login = ViewLogin.login_user()
    dicionario.deletar('login', login)

def telnet(child, ip, username, password, timeout=5):
    child.sendline("telnet {0}".format(ip))

    # Digita a senha TACACS
    child.expect(':', timeout=timeout)  # Espera Username
    child.sendline(username)

    child.expect(':', timeout=timeout)  # Espera Senha
    child.sendline(password)

    index = child.expect(['>', 'failed'], timeout=timeout)

    if index == 0:
        # Entra em modo privilegiado
        child.sendline("ena")
        child.sendline(password)
        index = child.expect(['#', '>'], timeout=timeout)
        if index == 0:
            print("Router Alcatel : Modo Privilegiado UP")
        if index == 1:
            print("Router Alcatel : Modo Privilegiado DOWN")
        return True
    if index == 1:
        # Digita a senha CPE-RMS
        # child.expect(':', timeout=timeout)  # Espera Username
        # child.sendline(username2)

        # child.expect(':', timeout=timeout)  # Espera Senha
        # child.sendline(password2)

        print("\n*** Epa! Nao conseguimos acessar ***")
        print("\tSenha ou usuario incorretos ... ")
        return



def telnet2(terminal, ip, username, password, timeout=5):
    terminal.child.sendline("telnet {0}".format(ip))

    # Digita a senha TACACS
    terminal.child.expect(':', timeout=timeout)  # Espera Username
    terminal.child.sendline(username)

    terminal.child.expect(':', timeout=timeout)  # Espera Senha
    terminal.child.sendline(password)

    index = terminal.child.expect(['>', 'failed'], timeout=timeout)

    if index == 0:
        # Entra em modo privilegiado
        terminal.child.sendline("ena")
        terminal.child.sendline(password)
        index = terminal.child.expect(['#', '>'], timeout=timeout)
        if index == 0:
            print("Router Alcatel : Modo Privilegiado UP")
        if index == 1:
            print("Router Alcatel : Modo Privilegiado DOWN")
        return True
    if index == 1:
        # Digita a senha CPE-RMS
        # child.expect(':', timeout=timeout)  # Espera Username
        # child.sendline(username2)

        # child.expect(':', timeout=timeout)  # Espera Senha
        # child.sendline(password2)

        print("\n*** Epa! Nao conseguimos acessar ***")
        print("\tSenha ou usuario incorretos ... ")
        return



class Server():
    
    @staticmethod
    def login(terminal):
        terminal.child.sendline('ssh ' + ip_servidor)    
        index = terminal.child.expect(['Login :', '>'], timeout=5)

        if index == 0:
            terminal.child.sendline(username)
        elif index == 1:
            print("\n*** Epa! Nao conseguimos acessar ***")
            print("\tVerifique se o IP esta correto ... ")
            return False

        terminal.child.expect('Senha :', timeout=5)
        terminal.child.sendline(password)

        index = terminal.child.expect(['01>', '!'], timeout=5)

        if index == 0:
            return True
        elif index == 1:
            print("\n*** Epa! Nao conseguimos acessar ***")
            print("\tSenha ou usuario incorretos ... ")
            return False
        



        







def iniciar():
    
    ViewBoasVindas.tela_de_boas_vindas()
    
    # ----- CARREGANDO/REGISTARNDO SERVER -----    
    
    dict_server = dicionario.ler('server')

    if not dict_server:
        ip = ViewServer.primeiro_acesso_server()
        dicionario.adicionar('server', '1', ip)
        dict_server = dicionario.ler('server')
        

    # ----- CARREGANDO/REGISTARNDO LOGIN -----

    dic_login = dicionario.ler('login')

    if not dic_login:
        login = ViewLogin.login_user()
        senha = ViewLogin.login_senha()
        dicionario.adicionar('login', login, senha)
        dic_login = dicionario.ler('login')
    
    # ----- DESEMPACOTANDO LOGIN E SERVER EM LISTA -----
    
    list_server = []
    for chave in dict_server:
        list_server.append(dict_server[chave])
        
    list_user = []
    list_senha = []
    for chave  in dic_login:
        list_user = chave
        list_senha = dic_login[chave]
        
    # ----- *** -----
    
    ViewBoasVindas.tela_de_conclusao_boas_vindas()
    
    # ----- *** -----
        
    while True:
        entrada = ViewMenuInicial.menu_inicial()
        
        if entrada == "1":
            # ----- INSTANCIANDO O TERMINAL -----
            terminal = Terminal()            
            terminal.terminal_simulacao(
                ip_servidor=list_server[0], username=list_user[0], password=list_senha[0])
            # terminal.terminal_real(
            #     ip_servidor=list_server[0], username=list_user[0], password=list_senha[0])

        if entrada == "9":
            pass

        if entrada == "0":
            exit()
    
    # ----- *** -----
    
    ip = entrada('Digite o IP')
    
    terminal.escreva(telnet, ip, list_user[0], list_senha[0])
    
    terminal.assumir_terminal()