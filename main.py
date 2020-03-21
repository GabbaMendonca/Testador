from terminal import Terminal

import config

import view
import server_teste
import pe_alcatel
import router_alcatel

'10.121.2.8'
class Config():
    def config_login(self):
        dic_ip = config.ler_dicionario('ip_server')

        if not dic_ip:
            ip = view.cadastrar_ip_server_testes()
            config.SERVER_TESTES['ip'] = ip
            config.gravar_dicionario(config.SERVER_TESTES, 'ip_server')
            dic_ip = config.ler_dicionario('ip_server')
            self.ip_server_teste = dic_ip
        else:
            self.ip_server_teste = dic_ip['ip']

            dic_login = config.ler_dicionario('login')

            if not dic_login:
                login = view.entrada("Por favor digite seu Login")
                senha = view.entrada_senha("Por favor digite sua Senha")
                config.LOGIN['login'] = login
                config.LOGIN['senha'] = senha
                config.gravar_dicionario(config.LOGIN, 'login')
                dic_login = config.ler_dicionario('login')
                self.login = dic_login['login']
                self.senha = dic_login['senha']
            else:
                self.login = dic_login['login']
                self.senha = dic_login['senha']


class Controller(Config):
    def __init__(self):
        self.terminal = Terminal()
        self._zerar_vrf_ip()

    def _executar(self, funcao, *args, **kwargs):
        imprimir = self.terminal.escreva(funcao, *args, **kwargs)
        if imprimir:
            view.ter_imprimir(imprimir)
            return True
        else:
            return False
    
    def _zerar_vrf_ip(self):
        self.vrf = None
        self.ip = None
    
    def _pegar_vrf_ip(self):
        if (self.vrf or self.ip) == None:
            self.vrf = view.entrada("Qual o VRF ?")
            self.ip = view.entrada("Qual o IP ?")

    def assumir_terminal(self):
        self.terminal.assumir_terminal()





    # --- SERVER TESTES ---
    def server_teste_login(self):
        self.config_login()
        resp = self._executar(
            server_teste.login,
            self.ip_server_teste,
            self.login,
            self.senha)

        if not resp:
            exit()



    # --- PE ALCATEL ---
    def ssh_alcatel_login(self):
        self.pe_borda_alcatel = view.entrada("\n\tQual o PE ?\n")
        resp = self._executar(
            pe_alcatel.login,
            self.pe_borda_alcatel,
            self.senha)

        if not resp:
            view.imprimir("PE Incorreto")

    
    def ssh_alcatel_ping(self):        
        self._pegar_vrf_ip()
        self._executar(
            pe_alcatel.ping,
            self.vrf,
            self.ip
        )

    
    def ssh_alcatel_bgp(self):        
        self._pegar_vrf_ip()
        self._executar(
            pe_alcatel.bgp,
            self.vrf,
            self.ip
        )

    def ssh_alcatel_logout(self):
            resp = self._executar(
                pe_alcatel.logout
            )

            if resp:
                print("Comando OK")

    def telnet(self):
        pass

    def ping(self):
        pass

    # --- ROUTER ALCATEL ---
    def router_alcatel_login(self):
        self._pegar_vrf_ip()
        self._executar(
            router_alcatel.login,
            self.vrf,
            self.ip,
            self.login,
            self.senha
        )

    def rodar_testes(self):
        resp = self._executar(
            router_alcatel.rodar_testes
        )

        if resp:
            print("Comando OK")

    def router_alcatel_logout(self):
        resp = self._executar(
            router_alcatel.logout
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

show router 5104 bgp summary neighbor 100.127.119.170
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

            if entrada == "9":
                self.c.assumir_terminal()

            if entrada == "0":
                exit()

            if entrada == "1":
                self.ssh_alcatel_pe()
                
            if entrada == "2":
                self.pe_telnet_cisco()
            



    # ---- PE'S DE BORDA ----
    # ---- ALCATEL ----
    def ssh_alcatel_pe(self):
        self.c.ssh_alcatel_login()

        while True:
            entrada = view.menu_ssh_alcatel()

            if entrada == "9":
                self.c.assumir_terminal()
            
            if entrada == "0":
                self.c.router_alcatel_logout()
                break

            if entrada == "1":
                self.ssh_alcatel_ping()

            if entrada == "2":
                self.ssh_alcatel_router()
                
            if entrada == "3":
                self.ssh_alcatel_bgp()
            

    def ssh_alcatel_ping(self):
        self.c.ssh_alcatel_ping()
    
    def ssh_alcatel_bgp(self):
        self.c.ssh_alcatel_bgp()



    # ---- CISCO ----
    def pe_telnet_cisco(self):
        while True:
            entrada = view.menu_nao_tem()

            if entrada == "9":
                self.c.assumir_terminal()

            if entrada == "1":
                pass
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass
        
    def ping(self):
        while True:
            entrada = view.menu_nao_tem()

            if entrada == "9":
                self.c.assumir_terminal()

            if entrada == "1":
                pass
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass


    # ---- ROUTERS'S ----
    def ssh_alcatel_router(self):
        self.c.router_alcatel_login()

        while True:
            entrada = view.menu_router_alcatel()

            if entrada == "9":
                self.c.assumir_terminal()

            if entrada == "0":
                self.c.router_alcatel_logout()
                break

            if entrada == "1":
                self.c.rodar_testes()
                self.c.assumir_terminal()
                
            if entrada == "2":
                pass

            if entrada == "3":
                pass

if __name__ == '__main__':
    main = Main()
