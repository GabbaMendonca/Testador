import dicionario
from view import ViewServer, ViewLogin, entrada
from terminal import Terminal


# ----- SERVER -----


def novo_server():
    server = dicionario.ler('server')

    if not server:
        return False

    num_server = (len(server) + 1)
    ip = ViewServer.server_ip()
    dicionario.adicionar('server', num_server, ip)


def carregar_server():
    server = dicionario.ler('server')

    if not server:
        ip = ViewServer.server_ip()
        dicionario.adicionar('server', '1', ip)
        return dicionario.ler('server')

    return server


def atulizar_server():
    server = ViewServer.server_nome()
    ip = ViewServer.server_ip()
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

def iniciar():
    server = carregar_server()
    login = carregar_login()

    l_server = list(server)
    l_login = list(login)

    terminal = Terminal()
    
    terminal.terminal_real(
        ip_servidor=server[l_server[0]], username=l_login[0], password=login[l_login[0]])
    
    ip = entrada('Digite o IP')
    
    terminal.escreva(telnet, ip, l_login[0], login[l_login[0]])
    
    terminal.assumir_terminal()