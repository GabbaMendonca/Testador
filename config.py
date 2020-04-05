import pickle #modulo pickle

#dicionário
LOGIN = {}

IP_SERVER_TESTES = {}

# ----- MANIPULR ARQUIVOS EXTERNOS -----
def gravar_dicionario(dicionario, nome_do_arquivo:str):
    try:    
        arq = open(nome_do_arquivo + '.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
    except:
        return False
    else:
        pickle.dump(dicionario,arq) #Grava uma stream do objeto "dic" para o arquivo.
        arq.close() #fechar o arquivo


def ler_dicionario(nome:str):
    try:
        arq = open(nome + '.txt','rb') #abrir o arquivo para leitura - o "b" significa que o arquivo é binário
    except FileNotFoundError:
        return False
    else:    
        dic = pickle.load(arq)#Ler a stream a partir do arquivo e reconstroi o objeto original.
        arq.close() #fechar o arquivo
        return dic #retorna o conteúdo do dicionário
    
    

# ----- MANIPULR ARQUIVOS EXTERNOS -----