import pickle #modulo pickle

# ----- MANIPULR ARQUIVOS EXTERNOS -----
class Dicionario():
    def gravar_dicionario(self, dicionario, nome_do_arquivo:str):
        try:    
            arq = open(nome_do_arquivo + '.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
        except:
            return False
        else:
            pickle.dump(dicionario,arq) #Grava uma stream do objeto "dic" para o arquivo.
            arq.close() #fechar o arquivo
            return True


    def ler_dicionario(self, nome:str):
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


class Dados_server(Dicionario):
    def __init__(self):
        self.server_testes = {}
        
    def criar_server(self, server, ip_server):
        """
        Obtem o IP de server de testes do usuario e adiciona em um dicionario
        """
        posicao = len(self.server_testes)
        self.server_testes[str(posicao)] = {
            'server': server, 'ip': ip_server}

    def ler_server(self):
        """
        Mostar a lista de servers do dicionario.
        """

        lista = []
        for x in self.server_testes:
            lista.append("Server : {0} - IP do Server : {1}".format(
                str(self.server_testes[x]['server']), self.server_testes[x]['ip']))

        return lista

    def atualizar_server(self, posicao, server, ip_server):
        """
        Atualiza o IP de um server no dicionario.
        """

        self.server_testes[str(posicao)] = {
            'server': server, 'ip': ip_server}

    def deletar_server(self, posicao):
        """
        Deleta o IP de um server no dicionario.
        """
        if int(posicao) == (len(self.server_testes) - 1):
            self.server_testes.pop(posicao)
            
        else:
            for x in self.server_testes:
                if int(x) >= int(posicao):   
                    y = (int(x) + 1)
                    
                    self.server_testes[x]['server'] = self.server_testes[str(y)]['server']
                    self.server_testes[x]['ip'] = self.server_testes[str(y)]['ip']
                    
                    if y == (len(self.server_testes) - 1):
                        self.server_testes.pop(str(y))
                        break
                    

    def carregar_server(self):
        """
        Tenta carregar o arquivo externo com o ip de server e retorna a validacao
        """

        self.server_testes = self.ler_dicionario('ip_server')

        if self.server_testes:
            return self.server_testes


    def gravar_server(self):
        """
        Grava o dicionario em arquivo externo
        """

        return self.gravar_dicionario(
            dicionario=self.server_testes, nome_do_arquivo='ip_server')


class Dados_login(Dicionario):
    def __init__(self):
        self.login = {}
        
        
    def criar_login(self, login, senha):
        """
        Obtem o login e senha do usuario e adiciona em um dicionario
        """

        posicao = len(self.login)
        self.login[str(posicao)] = {'login': login, 'senha': senha}

    def ler_login(self):
        """
        Mostar a lista de logins do dicionario.
        """

        lista = []
        for x in self.login:
            lista.append("Login : {0}".format(str(self.login[x]['login'])))

        return lista

    def atualizar_login(self, posicao, login, senha):
        """
        Atualiza o IP de um server no dicionario.
        """

        self.login[str(posicao)] = {'login': login, 'senha': senha}

    def deletar_login(self, posicao):
        """
        Deleta o IP de um server no dicionario.
        """

        if int(posicao) == (len(self.login) - 1):
            self.login.pop(posicao)
        else:
            for x in self.login:
                if int(x) >= int(posicao):
                    y = (int(x) + 1)
                    
                    self.login[x]['login'] = self.login[z]['login']
                    self.login[x]['senha'] = self.login[z]['senha']
                    
                    if y == (len(self.login) - 1):
                        y = y - 1
                        self.login.pop(str(y))
                        break

    def carregar_login(self):
        """
        Tenta carregar o arquivo externo com o ip de server e retorna a validacao
        """
        
        self.login = self.ler_dicionario('login')

        if self.login:
            return self.login

    def gravar_login(self):
        """
        Grava o dicionario em arquivo externo
        """

        self.gravar_dicionario(
            dicionario=self.login, nome_do_arquivo='login')