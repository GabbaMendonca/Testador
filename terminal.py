import pexpect

class Terminal():
    
    child = pexpect.spawn("python router_de_testes/router_testes.py")

    try:
        child.expect('>')
        print("TERMINAL OK")

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
    def interacao():
    
        try:
            Terminal.child.interact(escape_character=chr(95))

        except pexpect.EOF:
            print("EOF : Ops! Algo errado não esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT : Ops! Algo errado não esta certo !")

