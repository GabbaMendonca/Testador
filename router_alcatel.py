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


def logout(child, timeout=5):
    try:
        child.sendline("logout")
        child.expect(['#', '>'], timeout=timeout)
        return True
    except Exception:
        print("Ops! Não foi possivel dar logout !")

def rodar_testes(child, timeout=5):
    try:
        child.sendline("sh ver | i power | up")
        # child.expect(['#', '>'], timeout=timeout)
        
        child.sendline("sh ip bg su | i :")
        # child.expect(['#', '>'], timeout=timeout)
        
        child.sendline("sh ip int br")
        # child.expect(['#', '>'], timeout=timeout)
        
        child.sendline("sh int | i Last clearing")
        # child.expect(['#', '>'], timeout=timeout)
        
        child.sendline("sh int | i CRC")
        # child.expect(['#', '>'], timeout=timeout)
        
        child.sendline("sh int Serial0/0/0")
        # child.expect(['#', '>'], timeout=timeou\t)
        
        child.sendline("sh arp")
        # child.expect('#', timeout=timeout)

    except Exception:
        print("Ops! O caminho esta incorreto !")