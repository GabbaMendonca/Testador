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
