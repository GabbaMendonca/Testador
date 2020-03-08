from terminal import Terminal

import view
import server_teste
import pe_alcatel


class Controller():
    def __init__(self):
        self.terminal = Terminal()
        self.ip_server_teste = "10.121.2.8"

    def executar(self, funcao, *args, **kwargs):
        imprimir = self.terminal.escreva(funcao, *args, **kwargs)
        if imprimir:
            view.ter_imprimir(imprimir)
            return True
        else:
            return False

    # --- SERVER TESTES ---
    def server_teste_login(self):
        # Coleta os dados para Login
        while True:
            self.login = view.entrada("Por favor digite seu Login")
            self.senha = view.entrada_senha("Por favor digite sua Senha")

            resp = self.executar(
                server_teste.login,
                self.ip_server_teste,
                self.login,
                self.senha)

            if resp:
                break
            else:
                exit()

    # --- PE ALCATEL ---
    def ssh_alcatel(self):
        self.pe_borda_alcatel = view.entrada("Qual o PE ?")
        resp = self.executar(
            pe_alcatel.login,
            self.pe_borda_alcatel,
            self.senha)

        if not resp:
            view.imprimir("PE Incorreto")

    
    def pe_alcatel_ping(self, vrf, ip):
        self.executar(
            pe_alcatel.ping,
            vrf,
            ip
        )

    def telnet(self):
        pass

    def ping(self):
        pass

    # --- ROUTER ALCATEL ---
    def router_alcatel_login(self):
        pass


# ===================================
"""
ssh 10.121.2.8
Login : oi369932
Senha : 1234

PE DE BORDA
ssh cen-ce-ser-a01

ENDERECO DO ROUTER
vrf = 5104
ip = 100.127.119.170
"""

class Main():
    def __init__(self):
        self.c = Controller()
        self.server_teste()

    # ---- SERVER TESTES ----
    def server_teste(self):
        self.c.server_teste_login()

        while True:
            entrada = view.menu_server_testes()

            if entrada == "0":
                pass

            if entrada == "1":
                self.pe_ssh_alcatel()
                
            if entrada == "2":
                self.telnet()

            if entrada == "3":
                self.ping()



    # ---- PE'S DE BORDA ----
    def pe_ssh_alcatel(self):
        self.c.ssh_alcatel()

        while True:
            entrada = view.menu_ssh_alcatel()

            if entrada == "0":
                pass

            if entrada == "1":
                self.router_alcatel()
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass

    def telnet(self):
        while True:
            entrada = view.menu_ssh_alcatel()

            if entrada == "0":
                pass

            if entrada == "1":
                pass
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass
        
    def ping(self):
        while True:
            entrada = view.menu_ssh_alcatel()

            if entrada == "0":
                pass

            if entrada == "1":
                pass
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass
        
        # ---- ROUTERS'S ----

    def router_alcatel(self):
        self.c.router_alcatel_login()

        while True:
            entrada = view.menu_ssh_alcatel()

            if entrada == "0":
                pass

            if entrada == "1":
                pass
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass

if __name__ == '__main__':
    main = Main()
