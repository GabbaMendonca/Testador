def login(child, ip_servidor, username, password):

    child.sendline('ssh ' + ip_servidor)
    index = child.expect(['Login :', '>'], timeout=5)

    if index == 0:
        child.sendline(username)
    elif index == 1:
        print("\n*** Epa! Nao conseguimos acessar ***")
        print("\tVerifique se o IP esta correto ... ")
        return False

    child.expect('Senha :', timeout=5)
    child.sendline(password)

    index = child.expect(['01>', '!'], timeout=5)

    if index == 0:
        return True
    elif index == 1:
        print("\n*** Epa! Nao conseguimos acessar ***")
        print("\tSenha ou usuario incorretos ... ")
        return False