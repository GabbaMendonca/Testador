from terminal import Terminal

import view
import server_teste
import pe_alcatel
import router_alcatel


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
    
    def interacao(self):
        self.terminal.interacao()

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
        self.vrf = view.entrada("Qual o VRF ?")
        self.ip = view.entrada("Qual o IP ?")
        self.executar(
            router_alcatel.login,
            self.vrf,
            self.ip,
            self.login,
            self.senha
        )

    def rodar_testes(self):
        resp = self.executar(
            router_alcatel.rodar_testes
        )

        if resp:
            print("Comando OK")


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
                pass

            if entrada == "3":
                pass



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
            entrada = view.menu_nao_tem()

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
            entrada = view.menu_nao_tem()

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
            entrada = view.menu_router_alcatel()

            if entrada == "0":
                self.c.interacao()

            if entrada == "1":
                self.c.rodar_testes()
                self.c.interacao()
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass

if __name__ == '__main__':
    main = Main()
