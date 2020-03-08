def login(child, vrf, ip, username, password, timeout=5):
    child.sendline("telnet router {0} {1}".format(vrf, ip))

    # Digita a senha TACACS
    child.expect(':', timeout=timeout)  # Espera Username
    child.sendline(username)

    child.expect(':', timeout=timeout)  # Espera Senha
    child.sendline(password)

    index = child.expect(['>', 'failed'], timeout=timeout)

    if index == 0:
        # Entra em modo privilegiado
        child.sendline("ena")
        child.sendline(password)
        index = child.expect(['#', '>'], timeout=timeout)
        if index == 0:
            print("Router Alcatel : Modo Privilegiado UP")
        if index == 1:
            print("Router Alcatel : Modo Privilegiado DOWN")
        return True
    if index == 1:
        # Digita a senha CPE-RMS
        child.expect(':', timeout=timeout)  # Espera Username
        child.sendline("cpe-rms")

        child.expect(':', timeout=timeout)  # Espera Senha
        child.sendline("PaneNOT31@")

        print("\n*** Epa! Nao conseguimos acessar ***")
        print("\tSenha ou usuario incorretos ... ")
        return