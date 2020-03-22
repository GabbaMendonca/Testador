import pexpect

class Terminal():
    def __init__(self, teste=True):
        if teste:
            Terminal.terminal_simulacao()
        else:
            Terminal.terminal_real()

    @staticmethod
    def terminal_real():
        Terminal.child = pexpect.spawn('ls')
        try:
            Terminal.child.expect('venv')
            print("Terminal REAL - OK")

        except pexpect.EOF:
            print("EOF - TERMINAL : Ops! Algo errado nao esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT - TERMINAL : Ops! Algo errado nao esta certo !")

        except Exception:
            print("Ops! O caminho esta incorreto !")


    @staticmethod
    def terminal_simulacao():
        Terminal.child = pexpect.spawn("python router_de_testes/router_testes.py")

        try:
            Terminal.child.expect('>')
            print("Terminal SIMULADO - OK")

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