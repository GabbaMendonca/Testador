import pexpect

class Terminal():
    @staticmethod
    def terminal_real(ip_servidor, username, password):

        Terminal.child = pexpect.spawn('ssh ' + ip_servidor)
        try:
            index = Terminal.child.expect(['Login :', '-01>', '!'], timeout=5)

            if index == 0:
                Terminal.child.sendline(username)
            elif index == 1:
                print("Terminal REAL - OK")
                return True
            elif index == 2:
                print("\n*** Epa! Nao conseguimos acessar ***")
                print("\tVerifique se o IP esta correto ... ")
                return False

            Terminal.child.expect('Senha :', timeout=5)
            Terminal.child.sendline(password)

            index = Terminal.child.expect(['-01>', '!'], timeout=5)

            if index == 0:
                print("Terminal REAL - OK")
                return True
            elif index == 1:
                print("\n*** Epa! Nao conseguimos acessar ***")
                print("\tSenha ou usuario incorretos ... ")
                return False

        except pexpect.EOF:
            print("EOF - TERMINAL : Ops! Algo errado nao esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT - TERMINAL : Ops! Algo errado nao esta certo !")

        except Exception:
            print("Ops! O caminho esta incorreto !")


    @staticmethod
    def terminal_simulacao(ip_servidor, username, password):
        Terminal.child = pexpect.spawn("python router_de_testes/router_testes.py")

        try:
            Terminal.child.sendline('ssh ' + ip_servidor)
            index = Terminal.child.expect(['Login :', '-01>', '!'], timeout=5) # TODO : Pendente verificar erro do ip do server estiver errado

            if index == 0:
                Terminal.child.sendline(username)
            elif index == 1:
                print("Terminal SIMULADO - OK")
                return True
            elif index == 2:
                print("\n*** Epa! Nao conseguimos acessar ***")
                print("\tVerifique se o IP esta correto ... ")
                return False

            Terminal.child.expect('Senha :', timeout=5)
            Terminal.child.sendline(password)

            index = Terminal.child.expect(['01>', '!'], timeout=5) # TODO : Pendente verificar erro quando logiun e senha não bater

            if index == 0:
                print("Terminal SIMULADO - OK")
                return True
            elif index == 1:
                print("\n*** Epa! Nao conseguimos acessar ***")
                print("\tSenha ou usuario incorretos ... ")
                return False

        except pexpect.EOF:
            print("EOF - TERMINAL : Ops! Algo errado nao esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT - TERMINAL : Ops! Algo errado nao esta certo !")

        except Exception:
            print("Ops! O caminho esta incorreto !")


    @staticmethod
    def escreva(funcao, *args, **kwargs):
        try:
            if funcao(Terminal.child, *args, **kwargs):
                return str(Terminal.child.before + Terminal.child.after)

        except pexpect.EOF:
            print("EOF : Ops! Algo errado não esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT : Ops! Algo errado não esta certo !")

    
    @staticmethod
    def assumir_terminal():
    
        try:
            print("\n *** Terminal em modo interativo *** \n")
            Terminal.child.interact(escape_character=chr(95))

        except pexpect.EOF:
            print("EOF : Ops! Algo errado não esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT : Ops! Algo errado não esta certo !")