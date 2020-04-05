from terminal import Terminal

import config

import view
import server_teste
import pe_alcatel
import router_alcatel

'10.121.2.8'


class Config():

    # --- IP SERVER TESTES ---
    def criar_ip_server_teste(self, num_server, ip_sever):
        """
        Obtem o IP de server de testes do usuario e adiciona em um dicionario
        """

        config.IP_SERVER_TESTES[str(num_server)] = {
            'server': num_server, 'ip': ip_sever}

    def ler_ip_server_testes(self):
        """
        Mostar a lista de servers do dicionario.
        """

        lista = []
        for x in config.IP_SERVER_TESTES:
            lista.append("Server : {0} - IP do Server : {1}".format(
                str(config.IP_SERVER_TESTES[x]['server']), config.IP_SERVER_TESTES[x]['ip']))

        return lista

    def atualizar_ip_server_testes(self, num_server, ip_server):
        """
        Atualiza o IP de um server no dicionario.
        """

        self.criar_ip_server_teste(num_server, ip_server)

    def deletar_ip_server_testes(self, num_server):
        """
        Deleta o IP de um server no dicionario.
        """

        for x in config.IP_SERVER_TESTES:
            if int(x) >= num_server:
                y = int(x)
                y = y + 1
                z = str(y)
                config.IP_SERVER_TESTES[x]['ip'] = config.IP_SERVER_TESTES[z]['ip']
                if y == len(config.IP_SERVER_TESTES):
                    config.IP_SERVER_TESTES.pop(str(y))
                    break

    def carregar_ip_server_testes(self):
        """
        Tenta carregar o arquivo externo com o ip de server e retorna a validacao
        """

        config.IP_SERVER_TESTES = config.ler_dicionario('ip_server')

        if config.IP_SERVER_TESTES:
            return True
        else:
            return False

    def gravar_ip_server_teste(self):
        """
        Grava o dicionario em arquivo externo
        """

        config.gravar_dicionario(
            dicionario=config.IP_SERVER_TESTES, nome_do_arquivo='ip_server')

    # --- LOGIN E SENHA ---
    def criar_login_e_senha(self, login, senha):
        """
        Obtem o login e senha do usuario e adiciona em um dicionario
        """

        posicao = len(config.LOGIN)
        config.LOGIN[str(posicao)] = {'login': login, 'senha': senha}

    def ler_login_e_senha(self):
        """
        Mostar a lista de logins do dicionario.
        """

        lista = []
        for x in config.LOGIN:
            lista.append("Login : {0}".format(str(config.LOGIN[x]['login'])))

        return lista

    def atualizar_login_e_senhas(self, posicao, login, senha):
        """
        Atualiza o IP de um server no dicionario.
        """

        config.LOGIN[str(posicao)] = {'login': login, 'senha': senha}

    def deletar_login_e_senha(self, posicao):
        """
        Deleta o IP de um server no dicionario.
        """

        for x in config.LOGIN:
            if int(x) >= posicao:
                y = int(x)
                y = y + 1
                z = str(y)
                if y < len(config.LOGIN):
                    config.LOGIN[x]['login'] = config.LOGIN[z]['login']
                    config.LOGIN[x]['senha'] = config.LOGIN[z]['senha']
                else:
                    y = y - 1
                    config.LOGIN.pop(str(y))
                    break

    def carregar_login_e_senha(self):
        """
        Tenta carregar o arquivo externo com o ip de server e retorna a validacao
        """
        config.LOGIN = config.ler_dicionario('login')

        if config.LOGIN:
            return True
        else:
            return False

    def gravar_login_e_senha(self):
        """
        Grava o dicionario em arquivo externo
        """

        config.gravar_dicionario(
            dicionario=config.LOGIN, nome_do_arquivo='login')


class Controller(Config):
    def testes_simulados(self):
        self.config_login()
        self.terminal = Terminal()
        self.terminal.terminal_simulacao(
            self.ip_server_teste, self.login, self.senha)
        self._zerar_vrf_ip()

    def testes_reais(self):
        self.config_login()
        self.terminal = Terminal()
        self.terminal.terminal_real(
            self.ip_server_teste, self.login, self.senha)
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
            self.senha,
            self.login2,
            self.senha2
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

        while True:
            entrada = view.menu_inicial()

            if entrada == "1":
                teste = view.menu_terminal()

                if teste != "n":
                    self.c.testes_simulados()
                    self.server_teste()
                else:
                    self.c.testes_reais()
                    self.server_teste()

            if entrada == "9":
                self.configuracoes()

            if entrada == "8":
                self.c.assumir_terminal()

            if entrada == "0":
                exit()

    def configuracoes(self):
        while True:
            entrada = view.menu_configuracores()

            if entrada == "1":
                self.c.trocar_o_ip()

            if entrada == "2":
                self.c.trocar_a_senha1()

            if entrada == "3":
                self.c.trocar_a_senha2()

            if entrada == "0":
                break

    # ---- SERVER TESTES ----
    def server_teste(self):

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

            if entrada == "7":
                self.c.trocar_o_ip()
                self.c.trocar_a_senha1()
                self.c.trocar_a_senha2()

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
