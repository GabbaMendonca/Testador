def login(child, pe, password, timeout=5):

    child.sendline('ssh ' + pe)
    index = child.expect(
        ['password:', 'continue connecting (yes/no)?'], timeout=timeout)

    if index == 0:
        child.sendline(password)
        child.expect("#", timeout=timeout)
        return True

    elif index == 1:
        child.sendline('yes')
        child.expect('password: ', timeout=timeout)
        child.sendline(password)
        child.expect("#", timeout=timeout)
        return True

def logout(child, timeout=5):
    try:
        child.sendline("logout")
        child.expect(['#', '>'], timeout=timeout)
        return True
    except Exception:
        print("Ops! Não foi possivel dar logout !")

def ping(child, vrf, ip, count=None, size=None, timeout=10):
    if count:
        if size:
            child.sendline('ping router {0} {1} {2}'.format(vrf, ip, size))
        else:
            child.sendline('ping router {0} {1} {2} {3}'.format(vrf, ip, count, size))
    else:
        child.sendline('ping router {0} {1}'.format(vrf, ip))

    child.expect("#", timeout=timeout)
    return True

def bgp(child, vrf, ip, timeout=10):
    child.sendline('show router {0} bgp summary neighbor {1}'.format(vrf, ip))
    child.expect("#", timeout=timeout)
    return True