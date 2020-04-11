import pickle  # modulo pickle

def _guardar_dicionario(dicionario: dict, nome_do_arquivo: str):
    try:
        # abrir o arquivo para gravação - o "b" significa que o arquivo é binário
        arq = open(nome_do_arquivo + '.txt', 'wb')
    except:
        return False
    else:
        # Grava uma stream do objeto "dic" para o arquivo.
        pickle.dump(dicionario, arq)
        arq.close()  # fechar o arquivo
        return True

def _pegar_dicionario(nome: str):
    try:
        # abrir o arquivo para leitura - o "b" significa que o arquivo é binário
        arq = open(nome + '.txt', 'rb')
    except FileNotFoundError:
        return False
    else:
        # Ler a stream a partir do arquivo e reconstroi o objeto original.
        dic = pickle.load(arq)
        arq.close()  # fechar o arquivo
        return dic  # retorna o conteúdo do dicionário

def _adicionar_atualizar(dicionario: dict, chave: str, valor: str):
    dicionario[chave] = valor

def _deletar(dicionario: dict, chave: str):
    try:
        del dicionario[chave]
        return True
    except:
        return False
    


def adicionar_atualizar(nome: str, chave: str, valor: str):
    dic = _pegar_dicionario(nome)

    if not dic:
        dic = {}

    _adicionar_atualizar(dic, chave, valor)
    _guardar_dicionario(dic, nome)


def ler(nome: str):
    return _pegar_dicionario(nome)


def deletar(nome: str, chave: str):
    dic = _pegar_dicionario(nome)

    if not dic:
        return False

    if _deletar(dic, chave):
        _guardar_dicionario(dic, nome)
        return True

    return False